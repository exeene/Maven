from deep_translator import GoogleTranslator, single_detection

class LanguageSupport:
    """
    Provides translation support for multiple languages using Google Translator.
    
    Features:
    - Translate text between languages.
    - Detect the language of input text.
    - Dynamically change the target language.
    """

    def __init__(self, target_language="en"):
        """
        Initializes the LanguageSupport module.
        
        :param target_language: The target language for translations (default: English).
        """
        if not self._is_valid_language(target_language):
            raise ValueError(f"Invalid target language: {target_language}")

        self.target_language = target_language

    def set_language(self, new_language):
        """
        Changes the target language for translations.
        
        :param new_language: The new target language code (e.g., "es" for Spanish).
        """
        if not self._is_valid_language(new_language):
            raise ValueError(f"Invalid language code: {new_language}")

        self.target_language = new_language

    def detect_language(self, text):
        """
        Detects the language of the given text.
        
        :param text: The input text to analyze.
        :return: The detected language code (e.g., "fr" for French).
        """
        try:
            return single_detection(text, api_key="your_api_key")  # Optional: Use an API key if needed
        except Exception as e:
            return f"Error detecting language: {e}"

    def translate(self, text):
        """
        Translates the given text into the target language.
        
        :param text: The text to translate.
        :return: The translated text.
        """
        try:
            translator = GoogleTranslator(source="auto", target=self.target_language)
            return translator.translate(text)
        except Exception as e:
            return f"Translation error: {e}"

    @staticmethod
    def _is_valid_language(language_code):
        """
        Checks if a language code is valid for Google Translate.
        
        :param language_code: The language code to validate.
        :return: True if valid, False otherwise.
        """
        supported_languages = GoogleTranslator().get_supported_languages(as_dict=True)
        return language_code in supported_languages.values()
