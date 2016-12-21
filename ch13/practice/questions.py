def foo(a):
    def moo():
        print(a)
    return moo

a = 200

def poo():
    print(a)
    a = 100
