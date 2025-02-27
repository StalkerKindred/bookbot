#python3 main.py im lazy af

book_path = "books/frankenstein.txt"

def main():
    text = get_book_text(book_path)
    word_count = get_word_count(book_path)
    letter_count = get_letter_count(book_path)
    print(f"{word_count} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(path):
    string_of_letters = " ".join(get_book_text(path))
    counter = 0
    for i in string_of_letters:
        counter += 1
    return (counter)

def get_word_count(path):
    string_of_words = (get_book_text(path)).split()
    return len(string_of_words)

main()