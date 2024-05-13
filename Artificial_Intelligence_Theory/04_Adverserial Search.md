# Adverserial Search
Search where two or more agents compete for opposing goals.

# Search Algo1: Minimax
The Minimax algorithm is a decision-making algorithm commonly used in two-player turn-based games. Its primary purpose is to find the optimal move for a player, assuming that the opponent also makes optimal moves. The algorithm is called "Minimax" because it seeks to minimize the possible loss for a worst-case scenario (opponent's best move) and maximize the potential gain.

## Working
- Game Tree Representation:
  - Represents possible moves and outcomes as a tree structure.
  - Nodes alternate between player and opponent moves.

- Evaluation Function:
  - Assigns numerical values to terminal states.
  - Indicates desirability of outcomes for the current player.
  
- Maximization and Minimization:
  - Maximizing player aims to maximize score.
  - Minimizing player aims to minimize score.
  - Alternates between levels in the game tree.
  - 
- Backtracking:
  - Recursively explores the tree.
  - Chooses moves that lead to the minimum or maximum value.

- Pruning (Optional):
  - Alpha-Beta Pruning optimizes the search.
  - Eliminates unnecessary branches to reduce computation.
  
- Optimal Move Determination:
  - Considers both players' perspectives.
  - Aims to find the best move assuming optimal play by the opponent.

## Alpha-beta pruning
A method to prune out some branches in our minimax tree, that is guaranteed to be unused. This will lead to increased performance.

## Depth limited minimax
Here, we stop the tree at some constant depth value. At this point, the algorithm evaluates the evaluation using some other arbitary function, at a non-terminal state.