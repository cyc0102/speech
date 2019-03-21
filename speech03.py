import time
from gtts import gTTS
from pygame import mixer
import tempfile

def speak(sentence, lang):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts=gTTS(text=sentence, lang=lang)
        tts.save('{}.mp3'.format(fp.name))
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()

speak('ありがとう', 'ja')
time.sleep(3)
speak('恭喜發財,豬年行大運', 'zh-tw')
time.sleep(4)
speak('Hello World!', 'en')
time.sleep(3)

