# Search problem with one agent
The purpose of the AI is to find a path (a series of actions) that will take us from the initial state to the final state, by minimising the path cost.

- Node is the data structure that we are going to use to solve our problem
- Frontier will be used to see all the possible future states
- Visited will contain the set of visited/ explored states

## Node
In the search problem, each state is represented as a node in a graph. 

Each node has to keep track of:
- A state
- The parent state
- Action taken from the parent state to reach the current state
- Path cost

Such a system will help us backtrack the path from the final state, all the way to the initial state.

## Frontier
Set of all states that we can next explore, but haven't explored.

## Visisted
Set of states, that have aldready been explored. There is no reason to explore them anymore.

## Huristic Function
A heuristic function is commonly employed to estimate the cost or value associated with reaching a goal state from a given state.

# Search Algo 1: Depth-First search
- We use a stack as the frontier
- We go deep into the tree/graph before backtracking back 
- Might not find the optimal solution

# Search Algo 2: Breadth-First search
- We use a queue as frontier
- We explore the shallower nodes first, before going deeper
- Always find the optimal solution
- This is generally more faster to converge at a solution, if the solution tend to lie closer to the start.

# Search Algo 3: Greedy Best-First search
  - Expands the nodes that is closest to the nodes.
  - An informed search that uses a huristic value
  - Neednot give the optimal solution

# Search Algo 4: A* search
 - At each point, takes into account the sum of huristic value and current steps
   i.e, chooses the path with the lowest h(x) + f(x)
 - Optimal if:
   - h(x) is admissible (never overestimate true cost - either get it correctly or underestimate)
   - h(x) is consistent (huristic value of my current state should be higher than my successor - it should consistently go down as we approach the goal)
 - Tend to use up a lot of memory