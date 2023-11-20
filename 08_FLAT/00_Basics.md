https://www.nesoacademy.org/cs/04-theory-of-computation

# Automata Theory - Theory of Computaition
This area studies abstract machines or models that can perform computations. These include finite automata, pushdown automata, and Turing machines. It investigates the capabilities and limitations of these machines in solving various problems.

# Finite State Machine
A Finite State Machine (FSM) is a mathematical model used to design and describe the behavior of systems with a finite number of states. It is the simplest model of computation with limited memory. 

![Alt text](<Screenshot from 2023-11-20 19-49-04.png>)

## Regular Language
A language is called a regualar language if and only if a FSM recogonises it.

## Regular Grammar
- A grammar refers to a set of production rules that define the structure of a formal language. It is a mathematical formalism used to describe the syntax of a language. 
- A regular grammar is a type of formal grammar that generates a regular language. It is one of the simplest forms of grammars and is closely associated with regular languages, which can be recognized by finite automata. 

# DFA
A Deterministic Finite Automaton (DFA) is a specific type of Finite State Machine (FSM) that has a set of states, a set of transitions between these states, an initial state, and a set of accepting states. The key difference between a DFA and a general FSM is that in a DFA, for each combination of a current state and an input symbol, there is exactly one uniquely determined next state.
- The equivalence of a Deterministic Finite Automaton (DFA) and a Regular Grammar means that for every regular language recognized by a DFA, there exists a corresponding regular grammar that generates the same language, and vice versa.

# NFA
A Non-deterministic Finite Automaton (NFA) is another type of Finite State Machine (FSM), similar to a Deterministic Finite Automaton (DFA), but with a key difference in the transition function. In an NFA, for a given state and input symbol, there can be multiple possible transitions to different states or even no transition at all.
- Every DFA is a NFA, but not vice versa.
- For every NFA, there is an equivalent DFA.



