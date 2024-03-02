
def print_book():
    path_text = "books/frankenstein.txt"
    text = get_book_text(path_text)
    num_words = get_num_words(text)
    characters_dict = get_characters_dict(text)
    character_list = characters_sort_list(characters_dict)
    print(f"---The current report of {path_text}---")
    print(f"{num_words} words found within the document")
    print()


    for item_text in character_list:
        if not item_text["char"].isalpha():
            continue
        print(f"The '{item_text['char']} character was found {item_text['num']} times")

    print("--- End reprt ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_characters_dict(text):
    character_dict = {}
    for character in text:
        lower_case = character.lower()
        if lower_case in character_dict:
            character_dict[lower_case] += 1
        else:
            character_dict[lower_case] = 1
    return character_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()


def sort_on(dict):
    return dict["num"]


def characters_sort_list(num_characters):
    sort_list = []
    for num_character in num_characters:
        sort_list.append({"char": num_character, "num": num_characters[num_character]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list



if __name__ == "__main__":
    print_book()