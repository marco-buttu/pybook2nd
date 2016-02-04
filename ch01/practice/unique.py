def unique(sequence):
    """Restituisci il numero di caratteri unici di sequence."""
    result = 0
    for item in sequence:
        if sequence.count(item) == 1:
            result = result + 1
    return result
