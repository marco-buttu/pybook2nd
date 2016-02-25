def onlyone(sequence):
    unique_items = set()
    for item in sequence:
        unique_items.add(item)
    return len(unique_items)


def onlyone2(sequence):
    unique_items = set(sequence)  # Make a set from a sequence
    return len(unique_items)
