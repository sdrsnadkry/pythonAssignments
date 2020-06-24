def multiply(list):
    multiply = 1
    for n in list:
        multiply *= n

    return multiply


print(multiply([1, 2, 3, 4, 5]))
