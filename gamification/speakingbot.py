from pydub import AudioSegment
import speech_recognition as sr
import aiml
from gtts import gTTS
import telepot
from telepot.aio.loop import MessageLoop
from telepot.aio.delegate import pave_event_space, per_chat_id, create_open
import asyncio


class CleoBot(telepot.aio.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(CleoBot, self).__init__(*args, **kwargs)
        self.kernel = aiml.Kernel()
        self.kernel.learn("startup.xml")
        self.kernel.respond("load aiml b")

    async def on_chat_message(self, msg):

        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':

            r = self.generateaiml(msg['text'])
            text, urls = self.extract_urls(r)

            await bot.sendMessage(chat_id, text + "\n" + urls)
        else:
            ogg_file_id = msg["voice"]["file_id"]
            await bot.download_file(ogg_file_id, "fromtelegram.ogg")

            r, msg = self.analizza_audio(bot, chat_id, msg)

            if r is not None:

                with open('sst.mp3', 'rb') as file:

                    await bot.sendVoice(chat_id, file)
                    if r != "":
                        await bot.sendMessage(chat_id, r)
            else:
                await bot.sendMessage(chat_id, msg)

    def generateaiml(self, text):
        reply = self.kernel.respond(text)
        return reply

    def extract_urls(self, response):
        # separate urls
        start = 0
        text = ""
        urls = ""
        temp = 0
        while temp >= 0:
            try:
                temp = response.index("url{", start)
                if temp >= 0:
                    end = response.index("}", temp)
                    urls = urls + response[temp + 4:end] + " "
                    text = text + response[start:temp]
                    start = end + 1
            except Exception as e:
                temp = -1
        if text == "":
            text = response

        return text, urls

    def analizza_audio(self, bot, chat_id, msg):
        file_ogg = AudioSegment.from_ogg("fromtelegram.ogg")
        file_ogg.export("fromtelegram.wav", format="wav")

        # speech to text

        wav = sr.AudioFile("fromtelegram.wav")
        recogn = sr.Recognizer()
        with wav as source:
            audio = recogn.listen(source)

        urls = ""
        try:
            domanda = recogn.recognize_google(audio, language="it-IT")
            print("Trascrizione del file audio: " + domanda)
            response = self.generateaiml(domanda)

            text, urls = self.extract_urls(response)

            # text to speech
            tts = gTTS(text=text, lang='it')
            tts.save("sst.mp3")

        except Exception:
            print("Impossibile riconoscere del testo nel file audio analizzato")
            return None, "scandisci meglio la richiesta"

        return urls, None


bot = telepot.aio.DelegatorBot("TOKEN", [
    pave_event_space()(
        per_chat_id(), create_open, CleoBot, timeout=20),
])

loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot).run_forever())
print('Listening ...')

loop.run_forever()
