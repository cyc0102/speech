from gtts import gTTS
tts = gTTS(text='hello', lang='en')
tts.save("hello.mp3")
tts = gTTS(text='恭喜發財,紅包拿來', lang='zh-tw')
tts.save("hello2.mp3")
tts = gTTS(text='恭喜發財,紅包拿來', lang='zh-cn')
tts.save("hello3.mp3")
