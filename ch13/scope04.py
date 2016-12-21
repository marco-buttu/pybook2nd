from sys import platform
print(platform)

def foo():
    x = 100
    def moo():
        print(x)
    return moo
