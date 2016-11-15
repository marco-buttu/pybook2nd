def powsum(*argv: 'numbers', exp: int = 2) -> 'number':
    """
    Restituisci la somma delle potenze degli argomenti.

        >>> powsum(2, 5, exp=3)  # 2**3 + 5**3
        133

    Il valore di dafault dell'esponente è 2:

        >>> powsum(2, 5)  # 2**2 + 5**2
        29
    """
    return sum(item**exp for item in argv)
