def duplicate(list):
    unique = []

    for n in list:
        if n not in unique:
            unique.append(n)
    return unique

print(duplicate([1,2,1,3,2,4,5,5,5,6,7,8,1,5,9,0,])) 
