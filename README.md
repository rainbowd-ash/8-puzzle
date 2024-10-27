# Sliding Block Puzzle Solver

## Homework for my AI class
How does one solve a puzzle? Many interpretations, even more answers to each one. Mathematics, philosophy, religion... the list goes on. I'm just gonna use best-first and then A* to do it.

## Inversion Count is true
Sliding block puzzle states are split into two groups, and a state in one group cannot reach a state in the other.

It's true and it's called group theory.

## Heuristics

### Misplaced Tiles
Count the number of tiles that are not in the correct spot.

### Manhatten Distance
For each tile, count the number of linear squares away from the goal position.

### Linear Conflict
After manhatten distance, count up the number of tiles that are in each others' way linearly and add that on.
