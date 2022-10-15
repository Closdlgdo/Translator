from translate import Translator

languages = ['el', 'fr', 'es']

text = input('What would you like to translate? >> ')

for language in languages:
    translator = Translator(provide='libre', from_lang='en', to_lang=language)
    translation = translator.translate(text)
    print(f'{language}: {translation}')