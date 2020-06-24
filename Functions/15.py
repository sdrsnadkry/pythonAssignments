lists = [1,2,3,4,5,6,7,8,9,0]


even = list(filter(lambda x: x%2 == 0 , lists))
odd = list(filter(lambda x: x%2 != 0 , lists))

print("Even nos: ", even)
print("Even nos: ", odd)



