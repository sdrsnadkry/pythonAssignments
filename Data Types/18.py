def largest(list):
    max = list[0]

    for n in list:
        if n > max:
            max = n

    return max


print("Max number is: ", largest([1, 2, 3]))
