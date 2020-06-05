from fbchat import log, Client
import aiml

# Subclass fbchat.Client and override required methods
class EchoBot(Client):



    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            txt = message_object
            if '/start' in txt:
                response = 'ciao'
            elif 'alla prossima' in txt:
                response = 'Grazie e alla prossima '
            elif 'quando è stato fondato?' in txt:
                photo_url = "https://commons.wikimedia.org/wiki/File:Colonia_iulia_felix.jpg#/media/File:Colonia_iulia_felix.jpg"
                response = "dall'epigrafe rinvenuta si evince che la costruzione dell'anfiteatro risale al I II d.C."\
                           + photo_url
            else:
                response = generate_aiml(txt)

            self.send(response, thread_id=thread_id, thread_type=thread_type)




def generate_aiml(text):
    kernel = aiml.Kernel()
    kernel.learn("aiml/gladiator/startup.xml")
    kernel.respond("load aiml b")
    reply = kernel.respond(text)
    return reply

client = EchoBot("email", "password")
client.listen()