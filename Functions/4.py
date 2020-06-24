def reverse(string):
    rev = ''
    length = len(string)

    while length > 0:
        rev += string[length-1]
        length = length - 1

    return rev


print(reverse("abc"))


# or simply

# rev = string[::-1]
