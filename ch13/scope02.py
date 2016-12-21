a = 33

def foo():
    a = 'chandra'
    def moo():
        print(a)
    return moo


def compute(x):
    print(a + x)
