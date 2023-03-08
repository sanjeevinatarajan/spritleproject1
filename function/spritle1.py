
def zero(func = None):
    return 0 if not func else func(0)
def one(func = None):
    return 1 if not func else func(1)
def two(func = None):
    return 2 if not func else func(2)
def three(func = None):
    return 3 if not func else func(3)
def four(func = None):
    return 4 if not func else func(4)
def five(func = None):
    return 5 if not func else func(5)
def six(func = None):
    return 6 if not func else func(6)
def seven(func=None):
    return 7 if not func else func(7)
def eight(func = None):
    return 8 if not func else func(8)
def nine(func = None):
    return 9 if not func else func(9)

def plus(y):
    return lambda x: x+y
def minus(y):
    return lambda x: x-y
def times(y):
    return lambda  x: x*y
def divided_by(y):
    return lambda  x: x//y



print(seven(plus(five())))

print(five(plus(nine())))

print(six(divided_by(two())))

print(three(times(eight())))

print(five(times(five())))














