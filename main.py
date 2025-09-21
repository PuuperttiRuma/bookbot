from stats import get_word_count

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")

main()