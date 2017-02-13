from multiprocessing import Process
from io_bound import io_bound_task

p1 = Process(target=io_bound_task)
p2 = Process(target=io_bound_task)
p1.start()
p2.start()
