def add_string(string1, string2 ):
    result = string1[:2] + string2 + string1[2:]
    return result

print(add_string('[[]]','string'))