lists = [{'comp': 'a', 'model': 'a1', 'color': 'white'}, {'comp': 'c',
                                                          'model': 'c1', 'color': 'red'}, {'comp': 'b', 'model': 'b1', 'color': 'black'}]


sorted_lists = sorted(lists, key=lambda x: x['comp'])

print(sorted_lists)
