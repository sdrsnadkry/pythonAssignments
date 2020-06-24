def first_last(string):
    if len(string) < 2:
        return ""

    return string[0:2] + string[-2:]


print(first_last('IWORKSHOP'))
