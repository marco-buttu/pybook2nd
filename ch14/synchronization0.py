result = 0

def task():
    global result
    for i in range(10**6):
        result += 1

if __name__ == '__main__':
    task()
    task()
    print('result:', result)
