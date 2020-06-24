def count(string):
    upperCount = 0
    lowerCount = 0
    for l in string:
        if l.isupper():
            upperCount += 1
        elif l.islower():
            lowerCount += 1
        else:
            pass

    print("Upper string Count: ", upperCount,
          "\nLower String Count: ", lowerCount)


string = input("Enter a string: ")
count(string)
