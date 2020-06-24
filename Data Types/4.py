def swap(a, b):
    ba = b[:2] + a[2:]
    ab = a[:2] + b[2:]
    return ba + ' ' + ab

print(swap('first', 'second'))