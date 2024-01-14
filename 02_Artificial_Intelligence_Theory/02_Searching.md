# Searching
The common techniques to problem solving with AI are:
- Search algorithms
- Knowledge representation and reasoning
- Machine Learning(NLP + CV)
- Expert systems
- Genetric Algorithms, etc.

# Search Algorithms
General Purpose search algorithm can be classified into two:
 1. Uninformed /Blind search: Search where we have no information about the search space.
 2. Informed search: There is some sort of guidance to aid the search. This information will help us to form a heuristic, that will aid the search process.

# Problem solving
- Goal formulation, based on the current situation and the agent’s performance measure, is the first step in problem solving.
- Problem formulation is the process of deciding what actions and states to consider, given a goal.
- The process of looking for a sequence of actions that reaches the goal is called search.
- A search algorithm takes a problem as input and returns a solution in the form of an action
sequence. Once a solution is found, the actions it recommends can be carried out. This
is called the execution phase.Notice that while the agent is executing the solution sequence it ignores its percepts when choosing an action because it knows in advance what they will be. 

# Problem
Inorder to do this, we need a well defined form of the problem called state space. It includes:
 - Initial state: Starting state
 - ACTION(s): A fn that returns the set of all possible actions, given a state
 - RESULT(s,a): The transition function that takes in the current state and a possible action, and returns the new state.
 - GOAL_TEST(s): Returns if the given state is the goal state
 - PATH_COST(path): Assigns a numeric cost to a path

For some problems, we will also have
 - UTILITY(s): Returns the utility value if it(exists) of a given state

# Solution  
A solution to a problem is an action sequence that leads from the initial state to a goal state. Solution quality is measured by the path cost function. An optimal solution has the lowest path cost among all solutions.