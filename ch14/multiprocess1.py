import os
import psutil
from multiprocessing import Process


def show_pyprocesses():
    print('\nProcesso con PID', os.getpid())
    for process in psutil.process_iter():
        try:
            if process.name() == 'python':
                print(process.pid, process.cmdline())
        except psutil.NoSuchProcess:
            pass


if __name__ == '__main__':
    p = Process(target=show_pyprocesses)
    show_pyprocesses()
    p.start()
    p.join()
    show_pyprocesses()
