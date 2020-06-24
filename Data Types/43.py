tuples = ('I', 'W', 'X', 'o', 'r', 'k', 's', 'h', 'o', 'p')

list = list(tuples)
list.remove("X")

tuples = tuple(list)
print(tuples)
