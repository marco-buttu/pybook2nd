import multiprocessing
import psutil
import time


class MyProcess(multiprocessing.Process):

    def run(self):
        print(f'Sono il processo {self.pid}')
        time.sleep(2)


if __name__ == '__main__':
    p = MyProcess()
    p.start()

    for process in psutil.process_iter():
        try:
            if process.name() == 'python':
                print(process.pid, process.cmdline())
        except psutil.NoSuchProcess:
            pass
