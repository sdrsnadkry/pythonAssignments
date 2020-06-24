lists = [1,2,3,4,5,6,7,8,9,0]

square = list(map(lambda x: x**2, lists))

cube = list(map(lambda x: x**3, lists))


print("Squares: ", square)
print("Cubes: ", cube)