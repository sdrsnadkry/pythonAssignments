def same(strings):
    counter = 0
    if len(strings) < 2:
        return False
    for n in strings:
        if n[0] == n[-1]:
            counter += 1

    return counter


print(same(['404', 'abba', 'harmonium', 'roar']))
