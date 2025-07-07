import sys
from stats import get_word_count, get_character_counts, sort_dictionary

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]

    book_text = get_book_text(path)
    word_count = get_word_count(book_text)

    character_counts = get_character_counts(book_text)
    sorted_dictionary_list = sort_dictionary(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for dict in sorted_dictionary_list:
        print(f"{dict.get('char')}: {dict.get('num')}")

    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()