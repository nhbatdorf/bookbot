def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    report(book_path, text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(string):
    return len(string.split())

def count_char(text):
    prep_text = text.lower()
    count_dict = {}
    for character in prep_text:
        if character in count_dict:
            count_dict[character] += 1
        else:
            count_dict[character] = 1
    return count_dict

def sort_on(dict):
    return dict["num"]

def report(path, text):
    char_count = count_char(text)
    char_dict = []
    for char in char_count:
        if char.isalpha():
            new_entry = {"char": char, "num": char_count[char]}
            char_dict.append(new_entry)
    char_dict.sort(reverse=True, key=sort_on)

    print(f"--- Reporting on {path} ---")
    print(f"{word_count(text)} words found in the document")
    for char in char_dict:
        print(f"The '{char["char"]}' character was found {char["num"]} times")
    print("--- End Report ---")

main()