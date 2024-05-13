# Divide and conquer

Take a (big) problem and divide it into smaller parts. Now solve these parts. This is divide. Now take the output from these smaller problems and combine them to get the final output. This is the conquer step.
```
Basic Format:
    def DAC(P):
         if P is a small problem:
	        Execute(P)
         else:
	        Divide P into P1,P2 ... Pk
	        Apply DAC(P1), DAC(P2) ... DAC(Pk)
	        Combine [DAC(P1), DAC(P2) ... DAC(Pk)]
```

A lot of recursive programs follow this divide and conquer approach.
Eg: Merge sort


`In divide and conquer the divided parts will be disjoint. (In dynamic programming, we divide into mutually overlapping parts)`
