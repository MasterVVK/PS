import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Translator object to handle translations
translator = Translator()


def translate_text(text, dest_language="ru"):
    try:
        # Translate the text to the specified destination language
        translation = translator.translate(text, dest=dest_language)
        return translation.text
    except Exception as e:
        print(f"Translation Error: {e}")
        return text  # Return the original text if translation fails


# Updated get_english_words function to include translation
def get_english_words_with_translation():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Translate words and definitions to Russian
        translated_word = translate_text(english_words)
        translated_definition = translate_text(word_definition)

        return {
            "english_words": english_words,
            "word_translation": translated_word,
            "word_definition": word_definition,
            "definition_translation": translated_definition
        }
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Update word_game function to use translations
def word_game_translated():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words_with_translation()
        if not word_dict:
            print("Failed to get the word data. Please try again later.")
            break
        word = word_dict.get("english_words")
        word_translation = word_dict.get("word_translation")
        word_definition = word_dict.get("word_definition")
        definition_translation = word_dict.get("definition_translation")

        print(f"Значение слова ({word_definition}) - {definition_translation}")
        user = input(f"Что это за слово? ")
        if user.strip().lower() == word_translation.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word_translation}")

        play_again = input("Хотите сыграть еще раз? Да/Нет")
        if play_again.lower() != "да":
            print("Спасибо за игру!")
            break

word_game_translated()
