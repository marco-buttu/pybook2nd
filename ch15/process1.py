import psutil
for process in psutil.process_iter():
    try:
        if process.name() == 'python':
            print(process.pid, process.cmdline())
    except psutil.NoSuchProcess:
        pass
