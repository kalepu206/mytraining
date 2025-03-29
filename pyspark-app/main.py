from word_counter import WordCounter
from utils.text_cleaner import clean_text

def main():
    user_input = input("Enter a sentence: ")
    cleaned = clean_text(user_input)
    counter = WordCounter(cleaned)
    result = counter.count_words()
    for word, count in result.items():
        print(f"{word}: {count}")
        print("Remote version: GitHub edit made to main.py")

if __name__ == "__main__":
    main()
