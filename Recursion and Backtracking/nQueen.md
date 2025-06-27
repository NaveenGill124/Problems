# ♟️ N-Queens Problem

## What I Learned from This Problem

At first, this problem felt quite complex because it involves placing queens on a chessboard such that no two queens attack each other. I had to really think from scratch and understand how a queen moves — in rows, columns, and both diagonals.

To solve the problem, I learned and applied the concept of **backtracking**, which is a form of recursion where we try all possibilities and backtrack when we hit an invalid state.

### Key Concepts I Learned:
- How to approach constraint-based problems using **backtracking**
- How to **check for queen safety** in all directions (vertical, horizontal, and diagonals)
- How to **backtrack properly** by placing and removing queens during recursive calls
- How to build and manage a **2D board** and convert it to the required output format
- Importance of using **deep copies** (not shallow ones) when storing board states
- How to optimize diagonal checking using loops instead of brute force

Initially, I wrote a brute version without worrying about optimization. It helped me understand how the recursive structure flows and what each function does. After debugging and refining my base logic, I finally got a working and clean solution using proper safe checks and backtracking.

This problem really improved my understanding of recursive thinking, state tracking, and how to think like a problem solver from scratch.
