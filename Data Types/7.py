def longest(lists):
    new_list = []
    for n in lists:
        new_list.append((len(n), n))  # [(1,'a'), (3,'ccc), (2,'bb') ]
    new_list.sort()  # [(1,'a'), (2,'bb'), (3,'ccc) ]

    return new_list[-1][1]  #(3,'ccc')[1] = ccc


print(longest(["a", "ccc", "bb"]))
