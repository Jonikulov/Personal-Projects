import os
import time
import json
import requests
from io import BytesIO
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = '1'

from dotenv import load_dotenv
from pygame import mixer
import edge_tts

load_dotenv(dotenv_path="credentials.env")

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


def mohirai_tts(api_key, text):
    """Mohir.ai TTS (https://mohir.ai/developers/api/tts)"""

    url = 'https://mohir.ai/api/v1/tts'
    headers = {'Authorization': api_key, 'Content-Type': 'application/json'}
    data = {'text': text,
            'model': 'davron',  # jahongir
            'blocking': 'true'}

    resp = requests.post(url, headers=headers, data=json.dumps(data))
    if resp.status_code == 200:
        print(text)
        play_audio_buffer(requests.get(resp.json()['result']['url']).content)
        # print(resp.json())
    else:
        print(f"Request failed with status code {resp.status_code}: {resp.text}")


def muxlisa_tts(api_key, text):
    """Muxlisa.uz TTS"""

    resp = requests.post(
        url = "https://api.muxlisa.uz/v1/api/services/tts/",
        data = {"token": api_key,
                "speaker_id": 1,
                "text": text,
                "audio_format": "wav"})

    if resp.status_code == 200:
        print(text)
        play_audio_buffer(resp.content)
    else:
        print(f"Request failed with status code {resp.status_code}: {resp.text}")


def edgetts(voice, text):
    """Microsoft Edge online TTS."""

    VOICES = ["uz-UZ-MadinaNeural", "uz-UZ-SardorNeural"]

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


api_key = os.getenv("MOHIRAI_API_KEY")
text = "Sun'iy Intellekt va Ma'lumotlar Ilmi"
mohirai_tts(api_key, text)

api_key = os.getenv("MUXLISA_API_TOKEN")
text = "Dasturiy Ta'minot Muhandisi"
muxlisa_tts(api_key, text)

text = "Informatika va Axborot Texnologiyalari"
edgetts(1, text)