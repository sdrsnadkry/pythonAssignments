def poor_check(string):
    string_not = string.find('not')  # gives index of not
    string_poor = string.find('poor')  # gives index of poor

    if string_poor > string_not and string_not > 0 and string_poor > 0:
        string = string.replace(string[string_not:string_poor+4], 'good')
    else:
        return string

    return string


print(poor_check('The Lyrics is not that poor'))
print(poor_check('The Lyrics is poor'))
