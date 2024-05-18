# Voice Desktop Notifier
'''
# python text to speech free

+ pyttsx3

 elevenlabs: Antoni, Adam, Drew, Josh, Michael
 gTTS
 coquiTTS (https://github.com/coqui-ai/TTS)
 tensorflowTTS
 Larynx
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
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = '1'

from pygame import mixer


wav = r"D:\GitHub\JARVIS\voices\you have a new message sir.wav"
mp3 = r"D:\Cloud Backup\Theme of the Week 22  The Avengers Theme from Age of Ultron_320kbps.mp3"

def play_audio(audio_file):
    """Plays existing audio file."""
    mixer.init()
    mixer.Sound(audio_file).play()
    while mixer.get_busy():
        time.sleep(0.1)
    mixer.quit()

play_audio(mp3)



text1 = "I will speak this text."
text2 = "Starting system. Hello Sir! I'm JARVIS."
text3 = "This is a test of text-to-speech."

import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 175)
# engine.setProperty('volume', 0.7)

engine.say(text1)
# engine.save_to_file("Hello World", 'test.wav')
engine.runAndWait()
engine.stop()






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