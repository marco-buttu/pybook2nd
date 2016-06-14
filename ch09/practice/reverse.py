from copy import deepcopy


def reverse(lst):
    lst_copy = deepcopy(lst)
    lst_copy.reverse()
    return lst_copy
