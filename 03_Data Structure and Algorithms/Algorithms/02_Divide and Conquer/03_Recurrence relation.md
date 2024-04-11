# Recurrence Relation
A recurrence relation(or recurrences) is a way of `defining the terms of a sequence with respect to its previous terms`. It is a mathematical relationship or equation that expresses the value of a function at some point in terms of its values at previous points. 

`Representing a problem as a reccurence relation will help us calculate its complexity.`

# Solving Recurrence Relations
There are three main methods:
- `The substitution method`: We guess a bound and then use mathematical in-
duction to prove our guess correct.
- `The recursion-tree method`:  We convert the recurrence into a tree whose nodes represent the costs incurred at various levels of the recursion. We use techniques for bounding summations to solve the recurrence.
- `The master method`: Used to solve recurrences of the form: `T(n) = aT(n/b) + f(n)`, where a>=1, b>1.



#### Refer:
https://www.youtube.com/watch?v=x0n75VFd31U&list=PLxCzCOWd7aiHcmS4i14bI0VrMbZTUvlTa&index=10&pp=iAQB