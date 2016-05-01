def isclose(a, b, rel_tol, abs_tol):
    if rel_tol < 0 or abs_tol < 0:
        raise ValueError('le tolleranze devono essere non-negative.')
    else:
        abs_err = abs(a-b)
        rel_err = abs_err / max(abs(a), abs(b))
        return abs_err <= abs_tol and rel_err <= rel_tol
