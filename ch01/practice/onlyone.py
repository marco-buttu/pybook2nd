def onlyone(sequence):
    unique_items = set()
    for item in sequence:
        unique_items.add(item)
    return len(unique_items)
