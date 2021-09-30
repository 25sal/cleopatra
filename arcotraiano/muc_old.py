#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import datetime
import logging
import slixmpp
import string
import requests
import jsonpickle
import json

from threading import Thread
from muc_abstract import AbstractMUC
from getpass import getpass
from argparse import ArgumentParser
from shared_storage import User

class TimeChecker(Thread):
    SLEEP_TIME = 30

    def __init__(self, delay, muc):
        Thread.__init__(self)
        self.muc = muc
        self.delay = delay
        self.time_stamp_old = datetime.datetime.now()
        self.time_stamp_new = datetime.datetime.now()

    def updateTimestamp(self, time_stamp):
        self.time_stamp_old = self.time_stamp_new
        self.time_stamp_new = time_stamp

    def run(self):
        while True:
            delta = datetime.datetime.now() - self.time_stamp_new
            if delta.seconds > self.delay:
                self.updateTimestamp(datetime.datetime.now())
                self.muc.unactive_users()
                time.sleep(self.SLEEP_TIME)
                self.muc.late_user()
            time.sleep(self.SLEEP_TIME)

class MUC(AbstractMUC, slixmpp.ClientXMPP):
    API_PRIVATE_MSG = 'http://localhost:5005/webhooks/rest/webhook'
    PLAYERS_NUMBER = 2

    def __init__(self, jid, password, room, nick):
        self.time_checker = TimeChecker(120, self)
        self.time_checker.start()

        slixmpp.ClientXMPP.__init__(self, jid, password)
        self.room = room
        self.nick = nick

        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.private_message)
        self.add_event_handler("muc::{}::presence".format(self.room),
                           self.new_user)

    def start(self, event):
        self.get_roster()
        self.send_presence()
        self.plugin['xep_0045'].join_muc(self.room,
                                         self.nick)

    def new_user(self, presence):
        # Se l'utente non è già presente (è andato momentaneamente offline)
        if presence['muc']['nick'] != self.nick and jsonpickle.decode(requests.get('http://localhost:5000/userPresence/{}'.format(presence['muc']['nick'])).content) == None:
            # Aggiungo l'utente alla lista
            requests.post('http://localhost:5005/addNewUser/{}'.format(presence['muc']['nick']))
            # Invio messaggio di benvenuto
            self.send_message(mto=presence['from'].bare,
                              mbody="Benvenuto {}, sono Cleopatra, appena saranno entrati tutti i giocatori inizieremo".format(presence['muc']['nick']),
                              mtype='groupchat')
                
    def private_message(self, msg):
        if msg['mucnick'] != self.nick and msg['type'] == 'chat':
            nickname = str(msg['from']).replace("{}/".format(self.room), '')
            payload ={
                        "sender":nickname,
                        "message":msg['body']
                    }
            r = requests.post(self.API_PRIVATE_MSG, data=json.dumps(payload))
            text = r.json()[0]['text'].replace('USER_NAME', nickname)
            self.send_message(mto=msg['from'],
                            mbody=text,
                            mtype='chat')

 

if __name__ == '__main__':
    # Setup the command line arguments.
    parser = ArgumentParser()

    # Output verbosity options.
    parser.add_argument("-q", "--quiet", help="set logging to ERROR",
                        action="store_const", dest="loglevel",
                        const=logging.ERROR, default=logging.INFO)
    parser.add_argument("-d", "--debug", help="set logging to DEBUG",
                        action="store_const", dest="loglevel",
                        const=logging.DEBUG, default=logging.INFO)

    # JID and password options.
    parser.add_argument("-j", "--jid", dest="jid",
                        help="JID to use")
    parser.add_argument("-p", "--password", dest="password",
                        help="password to use")
    parser.add_argument("-r", "--room", dest="room",
                        help="MUC room to join")
    parser.add_argument("-n", "--nick", dest="nick",
                        help="MUC nickname")

    args = parser.parse_args()

    # Setup logging.
    logging.basicConfig(level=args.loglevel,
                        format='%(levelname)-8s %(message)s')

    if args.jid is None:
        args.jid = input("Username: ")
    if args.password is None:
        args.password = getpass("Password: ")
    if args.room is None:
        args.room = input("MUC room: ")
    if args.nick is None:
        args.nick = input("MUC nickname: ")

    # Setup the MUCBot and register plugins. Note that while plugins may
    # have interdependencies, the order in which you register them does
    # not matter.
    xmpp = MUC(args.jid, args.password, args.room, args.nick)
    xmpp.register_plugin('xep_0030') # Service Discovery
    xmpp.register_plugin('xep_0045') # Multi-User Chat
    xmpp.register_plugin('xep_0199') # XMPP Ping

    # Connect to the XMPP server and start processing XMPP stanzas.
    xmpp.connect()
    xmpp.process()
