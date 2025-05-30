from stats import count_words,count_characters,sorted_list_dict
import sys
def get_book_text(filepath):
    with open(filepath,'r',encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents


def main():
    

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")  
        sys.exit(1)

    filepath = sys.argv[1]

    book_text= get_book_text(filepath)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words ")
    print("--------- Character Count -------")
    character_counts = count_characters(book_text)
    dict_items = sorted_list_dict(character_counts)
    for entry in dict_items[:]:
        print(f"'{entry['char']}: {entry['num']}'")
    print("============= END ===============")


if __name__ == "__main__":
    main()
