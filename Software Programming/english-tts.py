"""
+ https://youtu.be/gVKbf31hrYs
+ https://home-assistant.io/integrations/microsoft/
+ https://learn.microsoft.com/en-us/azure/ai-services/speech-service/index-text-to-speech
+ https://home-assistant.io/integrations/yandextts/
+ https://home-assistant.io/integrations/watson_tts/
+ https://home-assistant.io/integrations/picotts/
+ https://home-assistant.io/integrations/amazon_polly/
+ https://home-assistant.io/integrations/google_cloud/#configuration
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
+ microsoft azure text to speech
+ microsoft edge text to speech
+ microsoft text to speech
"""

import os
import time
from io import BytesIO
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = '1'

from pygame import mixer
import pyttsx3
import edge_tts


def play_audio(audio_file):
    """Plays existing audio file."""
    mixer.init()
    mixer.Sound(audio_file).play()
    while mixer.get_busy():
        time.sleep(0.1)
    mixer.quit()


def play_audio_buffer(audio_data):
    """Plays audio data from a bytes-like object."""
    mixer.init()
    mixer.Sound(BytesIO(audio_data)).play()
    while mixer.get_busy():
        time.sleep(1)
    mixer.quit()


def pytts_offline(text, rate=175, volume=1, save_file=None):
    """Text-to-Speech offline."""

    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    print(text)
    engine.say(text)
    if save_file:
        engine.save_to_file("Hello World", 'test.wav')
    engine.runAndWait()
    engine.stop()


def edgetts(voice, text):
    """Microsoft Edge online TTS."""

    VOICES = [
        "en-CA-LiamNeural",
        "en-US-AndrewNeural",
        "en-US-ChristopherNeural",
        "en-US-EricNeural",
        "en-US-BrianNeural",
        "en-US-SteffanNeural",
        "en-US-RogerNeural",
        "en-US-GuyNeural",
        "en-GB-ThomasNeural",
        "en-GB-RyanNeural"
    ]

    communicate = edge_tts.Communicate(text, VOICES[voice])
    # communicate.save_sync("output.wav")
    audio_data = []
    for chunk in communicate.stream_sync():
        if chunk["type"] == "audio":
            audio_data.append(chunk["data"])
        # elif chunk["type"] == "WordBoundary":
        #     print(chunk["text"], end=" ")
    print(text)
    play_audio_buffer(b"".join(audio_data))


text = "I will speak this text."
# pytts_offline(text)

# text = "Computer Science and Information Technology."
# edgetts(0, text)
