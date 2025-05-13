# Unique Paths

What I learned from the “Unique Paths” problem:

Given an \(m x n\) grid, any path from the top-left to the bottom-right consists of exactly:  
- \((m - 1)\) down-steps (D)  
- \((n - 1)\) right-steps (R)  

In total you make  
\[
(m - 1) + (n - 1) \;=\; m + n - 2
\]  
moves.

---

## Example: \(2 x 3\) Grid

- **Down-steps needed:** \(1\)  
- **Right-steps needed:** \(2\)  
- **Total moves:** \(1 + 2 = 3\)  

The distinct sequences of moves are:

