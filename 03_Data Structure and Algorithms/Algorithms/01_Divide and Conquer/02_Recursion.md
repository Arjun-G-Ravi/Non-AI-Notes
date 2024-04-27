# Recursion
Recursion is a programming technique where a function calls itself, and this self-referential nature can be described mathematically through recurrence relations.

It solves a problem by calling a copy of itself to work on a smaller problem. Recursive code tend to be shorter and elegant. But every recursive step requires extra memory (iterative step does not) and hence recursive solutions tend to be less efficient than its iterative counterpart. 

	Basic Format:	def func(parameter):
				        if base_condition_involving_parameter:
				            return value
				        else:
				            return func(changed parameter)

## Call Stack
The call stack is a region of memory that stores information about the active subroutine(functions or methods) in a program. Each recursive call adds a new frame to the call stack. The stack keeps track of the local variables, parameters, and return addresses for each active function call.

### Stack Overflow:
It's important to note that excessive recursion without proper termination conditions can lead to a stack overflow, where the call stack runs out of available memory. This is why it's crucial to have a base case in recursive functions that ensures termination. 

## Steps to solving a recursive problem

![Alt text](<Screenshot from 2023-12-27 12-34-42.png>)

https://www.youtube.com/watch?v=IJDJ0kBx2LM&t=24s