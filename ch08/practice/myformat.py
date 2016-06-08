def myformat(number, width):
    # return f'{number:,.{width}f}'  # Python >= 3.6
    return '{0:,.{1}f}'.format(number, width)
