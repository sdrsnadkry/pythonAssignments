def factorial(num):
    fact = 1
    if num < 0:
        print("Factorial for negative number doesnot exists")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num+1):
            fact = fact*i

        print(fact)


num = int(input("enter a number: "))
factorial(num)
