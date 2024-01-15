# Basic Terminologies 

## 1. Agent
- An agent is just something that operate autonomously, perceive their environment, persist over a prolonged time period, adapt to change, and create and pursue goals. It can be viewed as perceiving its environment through sensors and acting upon that environment through actuators.
- Mathematically speaking, we say that an agent’s behavior is described by the agent function that maps any given percept sequence to an action.
  
###### Rationanl Agent
- Rational Agent: It is the agent that does the right thing. It is a specific type of intelligent agent that is not only capable of perceiving its environment, learning, and taking actions but also acts in a way that is expected to achieve the best outcome or maximize its utility.
- Rationality maximizes expected performance, while perfection maximizes actual performance.
- PEAS is an acronym that stands for Performance measure, Environment, Actuators, and Sensors. It is a framework used to describe the key components of an intelligent agent.


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

## 7. Path cost
A numerical value which represents the cost it takes to travel through a given path. 
ie, how costly is this path of actions

## 8. Solution
A sequence of action that takes us from initial state to final state. The optimal solution is the solution with the lowest possible path cost.

## 9. Percept Sequence
- An agent’s percept sequence is the complete history of everything the agent has ever perceived.
- An agent’s choice of action at any given instant can depend on the entire percept sequence observed to date, but not on anything it hasn’t perceived.

## 10. Policy
- A sequence of actions that takes an agent from the current state to the goal state.
- An action is considered to be good, if it is a part of a good policy
  
## 11. Environment
- Place where the agent acts
- It can be fully observable or partially observable