# Basic Terminologies 
## 1. Intelligent Agent
- An agent is just something that operate autonomously, perceive their environment, persist over a prolonged time period, adapt to change, and create and pursue goals. An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators.
- Mathematically speaking, we say that an agent’s behavior is described by the agent function that maps any given percept sequence to an action.

## 2. State
A "state" refers to the current situation or condition of a system at a specific point in time. The goal of an intelligent agent will be to move from initial state to final(expected) state.

## 3. Action
The choices made by the agent, which changes the state

We define a function to represent this in code.
ACTIONS(s) is the function that takes in current state, and output the possible actions

## 4.  Transition model
A description of what state results from performing one action on a state.
RESULT(s,a): Returns the state which occurs when we perform action a on state s.

## 5. State space
Set of all states reachable from initial state, by any sequence of actions. This can be visualised as a graph, where each node represent different states and edges represent different states.

## 6. Goal Test
A way to determine if the current state is a goal state

## 7.Path cost
A numerical value which represents the cost it takes to travel through a given path. 
ie, how costly is this path of actions

## 8. Solution
A sequence of action that takes us from initial state to final state. The optimal solution is the solution with the lowest possible path cost.

## Percept Sequence
- An agent’s percept sequence is the complete history of everything the agent has ever perceived.
- An agent’s choice of action at any given instant can depend on the entire percept sequence observed to date, but not on anything it hasn’t perceived.


# Search problem
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


# Search Algo 1: Depth-First search
- We use a stack as the frontier
- We go deep into the tree/graph before backtracking back 

# Search Algo 2: Breadth-First search
- We use a queue as frontier
- We explore the shallower nodes first, before going deeper