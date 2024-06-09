# Automata theory
This area studies abstract machines or models that can perform computations. These include finite automata, pushdown automata, and Turing machines. It investigates the capabilities and limitations of these machines in solving various problems.

By using mathematical models, we can strip away all of these superfluous details and better understand the capabilities of the underlying model. We’ll see that an surprisingly simple model of computation is capable of representing any computation.

The point of all this is not to come up with a blueprint for a real computer. The point is to find a mathematical model that is both simple to understand yet powerful enough to model any arbitrary computation. 

# Basic Terms

1. `Symbol`: A letter/ character. Eg: a,b ...
2. `Alphabet`(Σ): Set of symbols (to be used to make strings). Eg: Σ = {a, b, c}
3. `Strings`: Finite sequence of symbols from a given alphabet. For example, if Σ = {a, b}, then "aab", "bba", and "abab" are all strings over Σ.
4. `Language`: A language is a set of strings formed from a given alphabet, that follows a certain rule.
5. `Grammar`: A grammar is a formal device used to generate strings in a language. It is a set of production rules that define the structure of a language. It is the mathematical formalism used to describe the syntax of a language. 
6. `Automation`:  An automaton is a mathematical model of a machine that accepts or rejects strings based on certain rules. They are used to define and recognize languages. Eg: Finite Automata, Pushdown Automata, Turing Machines, etc.
   
### Note
- Φ often refers to an empty set or language
- ε refers to the empty string