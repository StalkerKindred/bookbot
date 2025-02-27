def get_word_count(path):
    string_of_words = (get_book_text(path)).split()
    return len(string_of_words)