def replace(string):
    result = string[-1:] + string[1:-1] + string[:1] 
    return result

print(replace('String'))