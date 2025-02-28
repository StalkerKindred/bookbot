#python3 main.py im lazy af
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    print("Books: frankenstein, mobydick, prideandprejudice")
    print("Paths: books/book.txt")
    sys.exit(1)

book_path = sys.argv[1]

from stats import get_book_text
from stats import get_word_count
from stats import get_letter_count
from stats import sorting

letter_dic = {}

def main():
    text = get_book_text(book_path)
    word_count = get_word_count(book_path)
    letter_count = get_letter_count(book_path)
    sorted_letter_dic = sorting(letter_dic)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in letter_count:
        if str.isalpha(i) == True:
            print (f"{i}:",letter_count[f"{i}"])
    print("============= END ===============")


main()