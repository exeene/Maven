# Voice Interaction Setup

## Enabling Voice Interaction

To enable voice interaction with your AI Waifu, follow these steps:

1. Import the `VoiceIntegration` class from `maven.core.voice_integration`.
2. Initialize the `VoiceIntegration` object with your OpenAI API key.
3. Use the `text_to_speech` and `speech_to_text` methods to interact with your AI Waifu via voice commands.

Example:

```python
from maven.core.voice_integration import VoiceIntegration

voice_integration = VoiceIntegration(api_key="your-api-key-here")
audio_url = voice_integration.text_to_speech("Hello, how can I assist you today?")
print(f"Audio URL: {audio_url}")
```
