from googletrans import Translator

translator = Translator()

def translate_text(text, target_language='es'):
    """Translate text to the target language."""
    try:
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        return f"Error in translation: {str(e)}"
