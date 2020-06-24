def multiply(list):
    result = 1

    for n in list:
        result *= n

    return result


print("Total: ", multiply([1, 2, 3]))
