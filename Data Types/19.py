def smallest(list):
    min = list[0]

    for n in list:
        if n < min:
            min = n
    return min


print("Smallest number is: ", smallest([1, 2, 3]))
