from pyneuphonic import Neuphonic, TTSConfig
from pyneuphonic.player import AudioPlayer
import os

api_key = "fd670d8dde423652a2b03922b9c3178a781191c6e5c51a3a5501ffbba752d2db.b572ca47-5ec5-461b-82a0-e28fefeed32f" # GET THIS FROM beta.neuphonic.com!!!!!!!!!

client = Neuphonic(api_key=api_key)
sse = client.tts.SSEClient()
tts_config = TTSConfig(speed=1.05,  voice='8e9c4bc8-3979-48ab-8626-df53befc2090', model="neu_hq")

with AudioPlayer() as player:
    response = sse.send("""Neuphonic generates high quality and low latency text to speech. Experience the speed and clarity of our dynamically powered voice synthesis by entering your text!""", tts_config=tts_config)
    player.play(response)
    # player.save_audio('output.wav') 