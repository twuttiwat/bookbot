def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    count_chars = {}
    for ch in text:
        lowered = ch.lower()
        if lowered in count_chars:
            count_chars[lowered] += 1
        else:
            count_chars[lowered] = 1
    return count_chars

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(dict_of_chars):
    sorted_char_counts = []
    for ch in dict_of_chars:
        char_count_item = {
            "char": ch,
            "num": dict_of_chars[ch]
        }
        sorted_char_counts.append(char_count_item)

    sorted_char_counts.sort(reverse=True, key=sort_on)
    return sorted_char_counts