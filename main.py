import sys
from stats import get_word_count, get_character_counts, sort_char_counts


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    text = get_book_text(path)
    word_count = get_word_count(text)
    character_counts = get_character_counts(text)
    sorted_char_counts = sort_char_counts(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_char_counts:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]
main()
