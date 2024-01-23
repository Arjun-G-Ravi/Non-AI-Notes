num = [i for i in range(10)]

even = lambda x: x%2==0 # Returns true for even numbers

even_test = [even(i) for i in num]
print(even_test)

print(any(even_test)) # or operator
print(all(even_test)) # and operator
