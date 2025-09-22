def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_counts(text):
    characters = {}
    text_lowercase = text.lower()
    for character in text_lowercase:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1

    return characters
