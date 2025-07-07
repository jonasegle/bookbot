def get_word_count(string):
    return len(string.split())

def get_character_counts(string):
    character_counts = {}
    lowercase_string = string.lower()
    unique_characters = set()

    for char in lowercase_string:
        unique_characters.add(char)
    
    for char in unique_characters:
        character_counts[char] = lowercase_string.count(char)
    return character_counts

def sort_dictionary(dict):
    list = []
    for char, num in dict.items():
        if char.isalpha():
            list.append({"char": char, "num": num})
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(items):
    return items["num"]