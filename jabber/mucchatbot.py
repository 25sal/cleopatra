import time
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import aioxmpp
from aioxmpp import MUCClient
from spade.message import Message
from spade.template import Template
import aiml
import datetime




class ReceiverAgent(Agent):

    class RecvBehav(CyclicBehaviour):
        async def run(self):
            # print("RecvBehav running")

            msg = await self.receive()  # wait for a message for 10 seconds
            if msg:
                # print(msg)
                if msg.body is not None:
                    # print("Message received with content: {}".format(msg.body))

                    response = msg.make_reply()
                    response.body = self.agent.kernel.respond(msg.body)
                    await self.send(response)

            # stop agent from behaviour
            # await self.agent.stop()

    def my_on_subscribe_callback(self, peer_jid):
        self.presence.approve(peer_jid)
        self.presence.subscribe(peer_jid)

    async def setup(self):
        print("ReceiverAgent started")
        self.presence.on_subscribe = self.my_on_subscribe_callback
        self.presence.set_available(show=aioxmpp.PresenceShow.CHAT)
        b = self.RecvBehav()
        # template = Template()
        # template.set_metadata("performative", "inform")
        self.add_behaviour(b)

        # aiml loading
        self.kernel = aiml.Kernel()
        self.kernel.learn("startup.xml")
        self. kernel.respond("load aiml b")

        # muc behavior
        self.language_selectors = [
             aioxmpp.structs.LanguageRange.fromstr('en'),
            aioxmpp.structs.LanguageRange.fromstr("*")
        ]

        self.mucservice = self.client.summon(aioxmpp.MUCClient)
        self.room, self.room_future  = self.mucservice.join(aioxmpp.JID("samnites", "conference.jabber.hot-chilli.net", None), "cleopatra2")

        self.room.on_message.connect(self._on_message)
        '''
        # eventually to be implemented
        
        room.on_topic_changed.connect(self._on_topic_changed)
        room.on_enter.connect(self._on_enter)
        room.on_exit.connect(self._on_exit)
        room.on_leave.connect(self._on_leave)
        room.on_join.connect(self._on_join)

        return client
        '''

    def _on_message(self, message, member, source, **kwargs):


        if member.direct_jid is not None:
            if member.direct_jid.localpart == self.jid.localpart and member.direct_jid.domain == self.jid.domain:
                return
        print("{} {}: {}".format(
            datetime.datetime.utcnow().isoformat(),
            member.nick,
            message.body.lookup(self.language_selectors),
        ))
        response = message.make_reply()
        text_body = message.body.lookup(self.language_selectors),
        response.body.update({aioxmpp.structs.LanguageTag.fromstr('en'): 'il multi chat non è supportato, scrivetemi direttamente in privato: cleopatra2@jabber.hot-chilli.net'})
        self.room.send_message(response)

    def my_on_subscribe_callback(self, peer_jid):
            self.presence.approve(peer_jid)
            self.presence.subscribe(peer_jid)


if __name__ == "__main__":
    receiveragent = ReceiverAgent("cleopatra2@jabber.hot-chilli.net", "password")

    future = receiveragent.start()
    future.result() # wait for receiver agent to be prepared.


    while receiveragent.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            receiveragent.stop()
            break
    print("Agents finished")
