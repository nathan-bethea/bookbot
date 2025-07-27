def count_words(text):
    count = len(text.split())
    return count

def count_chars(text):
    chars = {}
    for letter in text.lower():
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1
    return chars

def sort_on(items):
    return items["count"]

def build_char_obj_list(dict):
    dict_list = []
    for key in dict:
        if key.isalpha():
            obj = {
                "char" : key,
                "count" : dict[key]
            }
            dict_list.append(obj)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list