import time
from pygame import mixer
mixer.init()
mixer.music.load('hello.mp3')
mixer.music.play()
time.sleep(2)
mixer.music.load('hello2.mp3')
mixer.music.play()
time.sleep(4)


