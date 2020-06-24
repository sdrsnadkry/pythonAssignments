dict = {'a': 2, 'b': 4, 'c': 6}

def delete(key):
    del dict[key]
    return dict

print(delete('a'))