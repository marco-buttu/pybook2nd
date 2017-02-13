from threading import Thread
from io_bound import io_bound_task

t1 = Thread(target=io_bound_task)
t2 = Thread(target=io_bound_task)
t1.start()
t2.start()
