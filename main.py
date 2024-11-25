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

def report(path, text):
    
    print(f"--- Reporting on {path} ---")
    print(f"{word_count(text)} words found in the document")
    print("--- End Report ---")

main()