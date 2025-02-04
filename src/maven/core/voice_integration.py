import openai

class VoiceIntegration:
    """Handles text-to-speech (TTS) and speech-to-text (STT) functionalities using OpenAI."""
    
    def __init__(self, api_key):
        openai.api_key = api_key

    def text_to_speech(self, text):
        """Converts text to speech and returns an audio file URL."""
        try:
            response = openai.Audio.create(
                model="tts-1",
                input=text,
                voice="alloy"
            )
            return response.get("url", "Failed to generate speech.")
        except Exception as e:
            return f"Error in text-to-speech conversion: {e}"

    def speech_to_text(self, audio_file):
        """Converts speech from an audio file to text."""
        try:
            with open(audio_file, "rb") as audio:
                response = openai.Audio.transcribe(
                    model="whisper-1",
                    file=audio
                )
                return response.get("text", "Failed to transcribe audio.")
        except Exception as e:
            return f"Error in speech-to-text conversion: {e}"
