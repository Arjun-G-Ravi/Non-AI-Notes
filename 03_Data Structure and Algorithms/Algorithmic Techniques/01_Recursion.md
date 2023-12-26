# Recurrence Relation
A recurrence relation is a way of defining the terms of a sequence with respect to its previous terms. It is a mathematical relationship or equation that expresses the value of a function at some point in terms of its values at previous points. 

# Recursion
Recursion is a programming technique where a function calls itself, and this self-referential nature can be described mathematically through recurrence relations.

It solves a problem by calling a copy of itself to work on a smaller problem. Recursive code tend to be shorter and elegant. But every recursive step requires extra memory (every iterative step does not) and hence recursive solutions tend to be less efficient than its iterative counterpart. 
```
Basic Format:	def func():
				      if base condition:
				               return value
				      else:
				               return func(changed parameter)
```

