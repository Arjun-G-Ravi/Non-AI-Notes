# global x
x = 10
def func():
    x = globals()['x']
    x += 1
    print(x)

func()
print(x)