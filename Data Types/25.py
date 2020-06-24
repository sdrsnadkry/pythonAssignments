lists1 = [{1,2,3,4,5},{},{}]
lists2 = [{},{},{}]

print(all(not items for items in lists1))
print(all(not items for items in lists2))