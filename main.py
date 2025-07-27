from stats import count_words, count_chars, build_char_obj_list
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_dict = count_chars(book_text)
    char_obj_list = build_char_obj_list(char_dict)
    pretty_print_stats(book_path,word_count, char_obj_list)

def pretty_print_stats(path, word_count, char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    dict_range = len(char_counts)
    for obj in range(0,dict_range):
        print(f"{char_counts[obj]["char"]}: {char_counts[obj]["count"]}")
    print("============= END ===============")
        

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

main()