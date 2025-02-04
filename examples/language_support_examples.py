translator = LanguageSupport(target_language="es")  # Spanish
print(translator.translate("Hello, how are you?"))  
# Output: "Hola, ¿cómo estás?"

translator.set_language("fr")  # Switch to French
print(translator.translate("Hello, how are you?"))  
# Output: "Bonjour, comment ça va?"

detected_lang = translator.detect_language("Wie geht es dir?")
print(f"Detected Language: {detected_lang}")  
# Output: "de" (German)
