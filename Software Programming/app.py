# Voice Desktop Notifier
'''
# python text to speech free

- elevenlabs: Antoni, Adam, Drew, Josh, Michael
- gTTS
+ coquiTTS (https://github.com/coqui-ai/TTS)

+ tensorflowTTS
+ pyttsx3
+ Larynx
+ edge-tts
+ Google Cloud Text-to-Speech
+ https://github.com/KoljaB/RealtimeTTS
+ OpenAI TTS, faster whisper
+ StyleTTS - https://github.com/yl4579/StyleTTS2?t...
+ Eleven's Style TTS - https://github.com/IIEleven11/StyleTT...
+ Coqui TTS - https://github.com/coqui-ai/TTS
+ Daswers XTTS GUI - https://github.com/daswer123/xtts-fin...
+ Suno Bark - https://github.com/suno-ai/bark
+ VallE-X - https://github.com/Plachtaa/VALL-E-X
+ BARK AI: https://github.com/suno-ai/bark
+ https://youtu.be/gwrKk649-Pw

'''
# UNINSTALL: playaudio playsound gTTS gtts

import os
import time

from pygame import mixer

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = '1'

text = "This is a test of text-to-speech."
wav = r"D:\GitHub\JARVIS\voices\you have a new message sir.wav"
mp3 = "sound.mp3"
mp3 = r"D:\Cloud Backup\Kung Fu Panda Trilogy Ultimate Cut_320kbps.mp3"

mixer.init()
mixer.music.load(wav)
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)
mixer.quit()

# playaudio(mp3)
print("Done!")



# from winotify import Notification, audio


# def speak(text):
#     pass


# toast = Notification(app_id="My Smart Reminder",
#                      title="Cool Title",
#                      msg="There's a message for you!",
#                      duration="short")
# toast.set_audio(audio.SMS, loop=False)

# toast.show()
# text = "Starting system. Hello, sir! I'm JARVIS."
# speak(text)