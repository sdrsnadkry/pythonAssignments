def unique(lists):
    newList = []

    for item in lists:
        if item not in newList:
            newList.append(item)

    return newList


print(unique([1, 2, 3, 4, 1, 2, 4, 5, 7, 8]))
