
book_path = "books/frankenstein.txt"

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(path):
    string_of_words = (get_book_text(path)).split()
    return len(string_of_words)

def get_letter_count(path):
    string_of_letters = " ".join(get_book_text(path))
    counter = 0
    for i in string_of_letters:
        counter += 1
    return (counter)