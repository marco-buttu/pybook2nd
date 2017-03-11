from threading import Thread
from cpu_bound import cpu_bound_task

t1 = Thread(target=cpu_bound_task, args=(10**7,))
t2 = Thread(target=cpu_bound_task, args=(10**7,))
t1.start()
t2.start()
