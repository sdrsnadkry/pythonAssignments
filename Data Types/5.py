def replace():
    string = input('Enter a string')
    length = len(string)
    if length > 2:
        if string[-3:] == 'ing':
            string = string.replace('ing', 'ly')
        else:
            string += 'ing'
    return string


print(replace())
