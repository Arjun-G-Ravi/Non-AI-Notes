# Knowledge based agents
Agents that helps us reason by operating on internal representation of knowledge. They will have some algorithm that will help them to use the knowledge it have, inorder to do something.

## Knowledge base
A set of sentences known by our knowledge based agent.

## Sentence
Assertion about the world in a knowledge representation language

# Propositional Logic
Propositional logic, also known as propositional calculus, is a branch of classical logic that deals with the manipulation and analysis of propositions or statements. Propositions are statements that can be either true or false but not both. In propositional logic, these propositions are typically represented by variables and combined using logical connectives to form more complex statements.

## Logical Connectives
1. not
2. and
3. or
4. implication: if P is True, then Q is also True
5. biconditional: P and Q is the same

## Entailment(⊨)
A⊨B means that in every world where A is true, B is also true. We want our AI to read the knowledge base, and figure out the entailments.

## Inference
Process of deriving new sentences from old ones. 
Every inference is just: Does KnowledgeBase ⊨ P ?

Logic Rules, discrete math stuff like modus ponens, 
2.26