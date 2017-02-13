from multiprocessing import Process
from cpu_bound import cpu_bound_task

p1 = Process(target=cpu_bound_task, args=(10**7,))
p2 = Process(target=cpu_bound_task, args=(10**7,))
p1.start()
p2.start()
