def multiply(num):
    val = lambda a: a * num
    return val


result = multiply(4)
print("Final Result =", result(10))
