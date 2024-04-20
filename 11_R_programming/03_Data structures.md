# Vectors
Vectors are mutable datastructures that stores collection of items.
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

