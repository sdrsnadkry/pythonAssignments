def sum(list):
    sum = 0
    for n in list:
        sum += n
    return sum


print("The sum of item in list is: ", (sum([1, 2, 3, 4, 5, 6])))
