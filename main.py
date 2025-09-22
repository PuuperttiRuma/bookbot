from stats import get_word_count, get_character_counts


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")
    character_counts = get_character_counts(text)
    print("Character counts:")
    print(character_counts)


main()
