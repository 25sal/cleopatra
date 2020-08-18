import time
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import aioxmpp
from spade.message import Message
from spade.template import Template
import aiml


class ReceiverAgent(Agent):

    class RecvBehav(CyclicBehaviour):
        async def run(self):
            print("RecvBehav running")

            msg = await self.receive(timeout=100) # wait for a message for 10 seconds
            if msg:
                # print(msg)
                if msg.body is not None:
                    print("Message received with content: {}".format(msg.body))

                    response = msg.make_reply()
                    response.body = self.agent.kernel.respond(msg.body)
                    await self.send(response)
            else:
                print("Did not received any message after 10 seconds")

            # stop agent from behaviour
            # await self.agent.stop()

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

    def my_on_subscribe_callback(self, peer_jid):
        self.presence.approve(peer_jid)
        self.presence.subscribe(peer_jid)


if __name__ == "__main__":
    receiveragent = ReceiverAgent("cleopatra2@jabber.hot-chilli.net", "cleopatra..")

    future = receiveragent.start()
    future.result() # wait for receiver agent to be prepared.

    while receiveragent.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            receiveragent.stop()
            break
    print("Agents finished")