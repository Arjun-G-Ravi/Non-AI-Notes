# Algorithms
An algorithm is the step-by-step instructions to solve a given problem. 

### Algorithmic Analysis
The performance of an algorithm is measured from its execution time and memory requirement. This can be represented in a polynomial form as shown in figure. This notation is called asymptotic notation. There are three ways to show the complexity of an algorithm:
- Big O: Worst case
- Big Ω: Best case
- Big ϴ: Mixture of the above two. It shows the average case performance.

![Alt text](image.png)

Among these, the big O is the most important as it lets us know the upper bound or worst performance an algorithm can perform. 

#### Basic Things to know to calculate Complexity
- A loop that iterates 'n' times contributes a factor of 'n' to the complexity.
- Nested loops multiply the complexity by the number of nested levels.
- The following loop gives a time complexity of O(log(2) n)

```
while ct < 100:
    print(“Hello”)
     ct = ct * 2           # as this variable increases exponentially 
```
- Non looped statements do not contribute to time complexity. Eg: if-else, prints, inputs, etc.