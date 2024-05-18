import os
import time
import json
import requests
from io import BytesIO
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = '1'

from pygame import mixer
from dotenv import load_dotenv

load_dotenv(dotenv_path="credentials.env")

def play_audio_buffer(audio_data):
    """Plays audio data from a bytes-like object."""
    mixer.init()
    mixer.Sound(BytesIO(audio_data)).play()
    while mixer.get_busy():
        time.sleep(1)
    mixer.quit()


def muxlisa_tts(api_key, text):
    """Muxlisa.uz TTS"""

    resp = requests.post(
        url = "https://api.muxlisa.uz/v1/api/services/tts/",
        data = {"token": api_key,
                "speaker_id": 1,
                "text": text,
                "audio_format": "wav"})

    if resp.status_code == 200:
        play_audio_buffer(resp.content)
    else:
        print(f"Request failed with status code {resp.status_code}: {resp.text}")


def mohirai_tts(api_key, text):
    """Mohir.ai TTS (https://mohir.ai/developers/api/tts)"""

    url = 'https://mohir.ai/api/v1/tts'
    headers = {'Authorization': api_key, 'Content-Type': 'application/json'}
    data = {'text': text,
            'model': 'jahongir-neutral',  # davron-neutral
            'blocking': 'true'}

    resp = requests.post(url, headers=headers, data=json.dumps(data))
    if resp.status_code == 200:
        play_audio_buffer(requests.get(resp.json()['result']['url']).content)
        # print(resp.json())
    else:
        print(f"Request failed with status code {resp.status_code}: {resp.text}")


def edge_tts(api_key, text):
    """Microsoft Edge TTS"""

    resp = requests.post(
        url = "",
        data = {"token": api_key,
                "speaker_id": 1,
                "text": text,
                "audio_format": "wav"}
            )

    if resp.status_code == 200:
        play_audio_buffer(resp.content)
    else:
        print(f"Request failed with status code {resp.status_code}: {resp.text}")


api_key = os.getenv("MUXLISA_API_TOKEN")
text = "dasturiy ta'minot muhandisi"
edge_tts(api_key, text)
