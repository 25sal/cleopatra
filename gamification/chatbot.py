import telepot
import aiml
import time


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':

        name = msg["from"]["first_name"]
        txt = msg['text']
        photo_url = "https://commons.wikimedia.org/wiki/File:Colonia_iulia_felix.jpg#/media/File:Colonia_iulia_felix.jpg"

        if '/start' in txt:
            bot.sendMessage(chat_id, 'ciao')
        elif 'alla prossima' in txt:
            bot.sendMessage(chat_id, 'Grazie e alla prossima ' + name)
        elif 'quando è stato fondato?' in txt:
            bot.sendPhoto(chat_id, photo_url,
                          "dall'epigrafe rinvenuta si evince che la costruzione dell'anfiteatro risale al I II d.C.")
        else:
            print(msg["text"])
            r = generate_aiml(msg['text'], chat_id)
            if r is not None and r != "":
                html_message = r.replace("\\n", "\n")
                bot.sendMessage(chat_id, html_message)


def generate_aiml(text, chat_id):
    
    reply = kernel.respond(text)
    return reply


kernel = aiml.Kernel()
kernel.learn("startup.xml")
kernel.respond("load aiml b")
bot = telepot.Bot("TOKEN")

bot.message_loop(on_chat_message)


while 1:
    time.sleep(30)
