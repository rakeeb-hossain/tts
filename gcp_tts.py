import googleapiclient.discovery
import os 
def gcp_tts():
    client = googleapiclient.discovery.build("texttospeech", "v1")
    print(client)
