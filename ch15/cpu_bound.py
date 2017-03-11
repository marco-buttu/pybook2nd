def cpu_bound_task(n):
    counter = 0
    for i in range(n):
        counter += i % 100
