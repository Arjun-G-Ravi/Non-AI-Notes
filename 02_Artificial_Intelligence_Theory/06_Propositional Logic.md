
## Clause
A clause is a disjuction(connected by or's) of literals


## Conjuctive Normal Form (CNF)
A logical sentence that is a conjunction(connected by and's) of clauses.
- Any sentence can be converted into conjuctive normal form

## Conversion to CNF
 - Eliminate biconditionals
     - turn A↔︎B to (A→B)∧(B→A)
 - Eliminate implecations
   - turn A→B to ¬AvB
 - Move ¬ inward with Demorgan's law
 - Use distributuve law to distribute to CNF


## Inference by resolution
To check if KB(Knowldege base) entails(⊨) A, we prove either one of these
        - KB∧¬A is False
        - KB∧A is True


3.39