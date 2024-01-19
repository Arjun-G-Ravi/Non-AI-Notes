# global x
x = 10
def func():
    global x
    x =11
    print(x)

print(x)
func()