#python3 main.py im lazy af
from stats import get_book_text
from stats import get_word_count
from stats import get_letter_count

book_path = "books/frankenstein.txt"

def main():
    text = get_book_text(book_path)
    word_count = get_word_count(book_path)
    letter_count = get_letter_count(book_path)
    print(f"{word_count} words found in the document")

main()