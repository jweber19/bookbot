def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_char = char_count(text)
    print(f"{num_words} words found in the document.")
    print("Printing character count:")
    print(num_char)

    char_report = []
    for char, value in num_char.items():
        if char.isalpha():
            char_report.append({'char': char, 'num': value})
    
    char_report.sort(reverse=True, key=sort_on)
    print('--- Begin report ---')
    for item in char_report:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print('--- End report ---')


def sort_on(dict):
    return dict["num"]

def char_count(text):
    char_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()