from deep_translator import GoogleTranslator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

translated_dict = {
    word: GoogleTranslator(source='french', target='english').translate(word)
    for word in french_words
}

print(translated_dict)
