def prime(num):
    if num < 1:
        print("Prime not valid for negative number")

    elif num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")

num = int(input("Enter a number: "))
prime(num)