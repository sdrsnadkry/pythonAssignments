def sort(sequence):
    for word in sequence:
        words = sequence.split(",")

    print(",".join(sorted(words)))


sequence = input("Enter words seperated by comma: ")
sort(sequence)
