# Variable Declaration
```
var <- 10

10 -> cow # both directional arrows are allowed

3 ->> my_var # global assignment

var1 <- var2 <- var3 <- "cow" # Assign the same value to multiple variables 
```

# Datatypes

## 1. Number Datatypes
- x <- 10.5   # numeric
- y <- 10L    # integer
- z <- 3 + 5i # complex


# Operators
- :     Creates a series of numbers in a sequence	x <- 1:10
- %in%	Find out if an element belongs to a vector	x %in% y
- %*%	Matrix Multiplication	                    x <- Matrix1 %*% Matrix2

# if-else
```
if (b > a) {
  print("b is greater than a")
} else if (a == b) {
  print("a and b are equal")
} else {
  print("a is greater than b")
}
```

# AND(&) and OR(|)
```
if (a > b & c > a) print("Both conditions are true")
```

# While Loop
```
x <- 10

while (x>0){
    print('banana')
    x <- x - 1
    if (x == 7) next # next is the same as continue in python
    if (x == 3) break
}

```

# For loop
```
for (x in 1:10) print(x)

animals <- c('cow', 'goat')
for (animal in animals) print(animal)

```

# Custom Functions
```
my_function <- function() { 
    # write what the function does
}
```