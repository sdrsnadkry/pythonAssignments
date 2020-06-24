def even_check(list):
    even = []

    for n in list:
        if n % 2 == 0:
            even.append(n)

    return even


print(even_check([1, 2, 4, 6, 7, 9, 11, 15, 48, 68]))
