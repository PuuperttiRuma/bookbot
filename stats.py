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


def sort_on(items):
    return items["num"]


def sort_char_counts(char_counts):
    sorted_list = []
    for char_key in char_counts:
        char_dict = {
            "char": char_key,
            "num": char_counts[char_key],
        }
        sorted_list.append(char_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
