def fibonacci(n):
    """Genera numeri di fibonacci."""
    a, b = 0, 1
    while a < n:
         yield a
         a, b = b, a + b

def hailstone(n):
    """Genera una sequenza di hailstone."""
    sequence = []
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
    else:
        yield 1
