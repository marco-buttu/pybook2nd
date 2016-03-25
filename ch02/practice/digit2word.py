def digit2word(digit):
    digits = {0: 'zero', 1: 'uno', 2: 'due', 3: 'tre', 4: 'quattro'}
    try:
        return digits[digit]
    except KeyError:
        return 'unknown'


def digit2word_2nd(digit):
    digits = {0: 'zero', 1: 'uno', 2: 'due', 3: 'tre', 4: 'quattro'}
    return digits[digit] if digit in digits else 'unknown'


def digit2word_3rd(digit):
    if digit == 0:
        return 'zero'
    elif digit == 1:
        return 'uno'
    elif digit == 2:
        return 'due'
    elif digit == 3:
        return 'tre'
    elif digit == 4:
        return 'quattro'
    else:
        return 'unknown'
