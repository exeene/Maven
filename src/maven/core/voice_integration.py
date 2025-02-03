import openai

class VoiceIntegration:
    def __init__(self, api_key):
        openai.api_key = api_key

    def text_to_speech(self, text):
        response = openai.TTS.create(text=text)
        return response.audio_url

    def speech_to_text(self, audio_file):
        response = openai.Whisper.transcribe(audio_file=audio_file)
        return response.text