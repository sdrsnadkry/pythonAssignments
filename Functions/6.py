def check(num):
    if num in range(2, 5):
        print("%s is in range" % str(num))
    else:
        print("%s is not found in range" % str(num))


num = int(input("Enter a number: "))
check(num)
