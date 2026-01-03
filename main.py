import sys

from stats import (
    get_num_words,
    get_chars_dict,
    chars_dict_to_sorted_list
)

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_path = sys.argv[1]
  text = get_book_text(book_path)
  count_words = get_num_words(text)
  count_chars = get_chars_dict(text)
  chars_sorted_list = chars_dict_to_sorted_list(count_chars)
  print_report(book_path, count_words, chars_sorted_list)

def get_book_text(file_path):
  with open(file_path) as f:
    return f.read()

def print_report(book_path, count_words, chars_sorted_list):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {count_words} total words")
  print("--------- Character Count -------")
  for item in chars_sorted_list:
    if item['char'].isalpha():
        print(f"{item['char']}: {item['num']}")

  print("============= END ===============")


main()