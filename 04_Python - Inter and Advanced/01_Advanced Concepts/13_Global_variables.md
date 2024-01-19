# Global fn in python

In Python, the need to declare a variable as global inside a function during recursion depends on whether you are modifying the variable's value within the function. When you declare a variable outside a function, it is considered a global variable, and you can usually access it within functions without using the global keyword if you are only reading its value.

However, if you intend to modify the value of a global variable inside a function, you need to use the global keyword. This is necessary because Python assumes that any variable assigned a value inside a function is a local variable unless specified otherwise. If a local variable has the same name as a global variable, the local variable takes precedence within the function scope.

In the context of recursion, if you have a recursive function and you are modifying a global variable within that function, you would still need to use the global keyword to indicate that you are referring to the global variable and not creating a new local variable at each recursive call. If you're only reading the global variable, then you may not need the global keyword inside the function.

For Eg:

```
x = 10
def func():
    print(x)

# This works without error as we are trying to just access the global variable from within a function.
```

```
x = 10
def func():
    x = 11
    print(x)

# Here, x is changed to 11 inside the function. So, outside the function, x is still 10.
```

```
x = 10
def func():
    global x
    x = 11
    print(x)

def func():
    global x
    x += 1
    print(x)

# These fns changes both x to 11, global and local.
```

But you don't want to do global in functions because, ideally, functions are not meant to change global variables. It also extends the scope, which can result in unforseen situations, as in https://www.youtube.com/watch?v=UEuXQjPUwcw.

# Globals
It lets you access global variables and change it the way you want, without affecting global.
```
x = 10
def func():
    x = globals()['x']
    x += 1
    print(x)

func()
print(x)
```
For more, watch https://www.youtube.com/watch?v=QYUbLevwgDQ