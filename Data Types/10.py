def replace_odd(string):
    result = ''
    length = len(string)

    for n in range(length):
        if n % 2 == 0:
            result = result + string[n]
    
    return result


print(replace_odd('String'))