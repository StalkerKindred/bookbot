
book_path = "books/frankenstein.txt"

letter_dic = {}

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(path):
    string_of_words = (get_book_text(path)).split()
    return len(string_of_words)

def get_letter_count(path):
    string_of_letters = " ".join(get_book_text(path))
    string_of_letters = str.lower(string_of_letters)
    for i in string_of_letters:
        if i in letter_dic:
            letter_dic[f"{i}"] += 1
        elif i not in letter_dic:
            letter_dic[f"{i}"] = 1
    return letter_dic

def sorting(letter_dic):
    sorted_letter_dic = sorted(letter_dic.items(), key=lambda x:x[1], reverse=True)
    back_to_dic = dict(sorted_letter_dic)
    return back_to_dic
