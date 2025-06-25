from google.cloud import translate_v2 as translate

# Initialize client
translate_client = translate.Client()

# Input text
text = "Hello, how are you?"

languages = ['es', 'fr', 'de','ur','hi','bn','ta','te','ml','kn','gu','mr','pa','ne','sd','si','ps','fa','ar','he','tr','ru','uk','bg','ro','hu','cs','sk','pl','sl','hr','sr','bs','mk','sq','el','it','pt','nl','da','sv','no','fi','et','lv','lt','mt','ga','cy','eu']
for lang in languages:
    translation = translate_client.translate(text, target_language=lang)
    print(f"Translated into {lang}: {translation['translatedText']}")
