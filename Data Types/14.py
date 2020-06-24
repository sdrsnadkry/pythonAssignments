def tags(tag, char):
    result = "<%s>%s<%s>" % (tag, char, tag)
    return result


print(tags('i', 'String'))
