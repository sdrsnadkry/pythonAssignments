def last(num):
    return num[-1]

def sort(tuples):
    return sorted(tuples, key=last)



print(sort([(1,3),(1,2),(6,0), (4,5)]))