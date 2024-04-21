# 1. Vectors
Vectors are mutable data structures that stores collection of items.
```
fruits <- c("banana", "apple", "orange")

a <- 1.5:6.2 # creates vector with (1.5 2.5 3.5 4.5 5.5)
```
### Functions
- length(v): To find len of vector
- sort(v): To sort the vector
- rep(v, each=no_times_to_be_repeated_for_each_elemt_on_v)
- seq(form=start_no, to=stop_no, by=step_size)

### Indexing
- R's indexing starts from 1
```
# Let v be a vector
v[1]: first element (0th elemt in classic programming)
v[-1]: all elements except the first one
v[1:100]: all elements from 1 to 100 (: creates a vector) # if there are no enough elements, NA appears at those indices
v[c(1,100)]: elements 1 and 100
```

# 2. Lists
A list in R can contain many different data types inside it. A list is a collection of data which is ordered and mutable.

- Initialised as l <- list("cow", "12", 24.4)
- List can be indexed as l[1]
- Mutable as 'goat' -> l[2]

## Functions
- length()
- "element" %in% l: To see if an element in a list
- append(l, new_element)
- Remove elements using negative indexing l = l[-1] # remove 1st element
- list3 <- c(list1,list2) # To join two lists


# 3. Matrices
A matrix is a two dimensional data set with columns and rows.They  are limited to two dimension.

- Initialised as mat <- matrix(c(1,2,3,'cow',5,6), nrow = 3, ncol = 2)
- Index as 
  - mat[1][2]
  - mat[2,] # the whole row
  - mat[c(1,2),] # select all of 1st and 2nd row

### Functions
- cbind(): To add a new column
- rbind(): To add a new row
```
mat <- matrix(c(1,2,3,4,5,6,7,8,9), nrow=3)
mat <- cbind(mat, c('cow', 'goat', 'elepahnt'))
```
- c() along with negative indexing to remove the rows and columns
```
mat[,c(-4, -2)]
```
- "item" %in% mat: Check if item in matrix
- dim(matrix): To see shape of the matrix
- nrow(), ncol(): To see dim of row and column
- rbind(), cbind(): To combine two matrices

# 4. Arrays
- Homogeneous
- multi-dimensional data structure
- array() to initialise
- dim() to see dimension