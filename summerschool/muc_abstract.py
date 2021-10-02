#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import slixmpp
import threading
import time
import datetime
import requests
import jsonpickle
import json
import string

from abc import ABC, abstractmethod

class AbstractMUC(ABC, slixmpp.ClientXMPP):
    API_PRIVATE_MSG = None
    time_to_unactive = None
    time_stamp_old = datetime.datetime.now()
    time_stamp_new = datetime.datetime.now()

    @abstractmethod
    def __init__(self,
                    API_PRIVATE_MSG,
                    jid,
                    password,
                    room,
                    nick,
                    seconds_to_unactive,
                    heartbeat):
        self.API_PRIVATE_MSG = API_PRIVATE_MSG
        self.seconds_to_unactive = seconds_to_unactive

        slixmpp.ClientXMPP.__init__(self, jid, password)
        self.room = room
        self.nick = nick

        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.private_message)
        self.add_event_handler("muc::{}::presence".format(self.room),
                           self.new_user)

        thread = threading.Thread(target = self.unactive_users)
        thread.daemon = True
        thread.start()

        if heartbeat:
            thread = threading.Thread(target = self.periodic_function)
            thread.daemon = True
            thread.start()

    def start(self, event):
        self.get_roster()
        self.send_presence()
        self.plugin['xep_0045'].join_muc(self.room,
                                         self.nick,
                                         wait=True)


    def new_user(self, presence):
        if presence['muc']['nick'] != self.nick:
            payload ={
                    "sender":"new_user",
                    "message":"NEW_USER {}".format(presence['muc']['nick'])
                }
            r = requests.post(self.API_PUBBLIC_MSG, data=json.dumps(payload))
            text = r.json()[0]['text'].replace('USER_NAME', msg['mucnick'])
            #Ritorno la risposta nella chat
            self.send_message(mto=self.room,
                          mbody=text,
                          mtype='groupchat')

    def private_message(self, msg):
        if msg['mucnick'] != self.nick and msg['type'] == 'chat':
            nickname = str(msg['from']).replace("{}/".format(self.room), '')
            payload ={
                        "sender":nickname,
                        "message":msg['body']
                    }
            r = requests.post(self.API_PRIVATE_MSG, data=json.dumps(payload))
            print(r.json())
            text = r.json()[0]['text'].replace('USER_NAME', nickname)
            self.send_message(mto=msg['from'],
                            mbody=text,
                            mtype='chat')

 