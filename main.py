# from collections import Counter

# with open("books/frankenstein.txt") as f:
#     files_data = f.read()
#     files_data = files_data.lower()

# words = files_data.split()
# print(words)
# print(f"On the book, there are a total of {len(words)} words")

# count_letters = Counter(files_data)
# print (count_letters)

# for letter, value in count_letters.items():
#     print (f"{letter}:{value}")

book_path = "books/frankenstein.txt"


def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    lista = get_characters_list(chars_dict)
    
    filtered_dict = {k: v for k, v in chars_dict.items() if 'a' <= k <= 'z'}
    sorted_chars = sorted(filtered_dict.keys())
    
    with open("report.txt", "a") as report:
        report.write('\n'f"--- Begin report of {book_path}. --- " '\n')
        report.write(f"{num_words} words was found in the book" '\n')
        for char in sorted_chars:
            line=(f"The character '{char}' was found {filtered_dict[char]} times" '\n')
            print(line)
            report.write(line)
        report.write("--- End report ---")

    print("Report ended successfully")
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_character_sums(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(book_path) as f:
        return f.read()


def get_characters_list(text):
    list_ch = list(text)
    sorted_list = sorted(list_ch)
    return sorted_list


main()