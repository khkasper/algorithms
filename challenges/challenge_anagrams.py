def string_dict(string):
    string_dict = {}
    for char in string.lower():
        if char in string_dict:
            string_dict[char] += 1
        else:
            string_dict[char] = 1
    return string_dict


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    first_string_dict = string_dict(first_string)
    second_string_dict = string_dict(second_string)
    if first_string_dict != second_string_dict:
        return False
    return True
