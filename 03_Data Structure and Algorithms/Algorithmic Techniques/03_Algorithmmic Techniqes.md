
# 2.Backtracking
Backtracking is a more refined and optimized version of brute force that intelligently explores the search space, avoiding unnecessary work whenever possible. This is done by generating a state space trees and searching for a solution via Depth First Search. Backtracking speeds the exhaustive search by cutting tree branches selectively (pruning). 

# 3. Divide and conquer
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
