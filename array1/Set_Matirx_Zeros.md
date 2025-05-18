## What I learned

### Set Matrix Zeros

When solving the “Set Matrix Zeroes” problem, it’s tempting to jump straight into a brute-force solution, but stepping back to analyze the optimal approach really pays off. Instead of zeroing out rows and columns repeatedly for every zero found (which can cost **O(M·N·(M+N))** time in the worst case), we scan the matrix once to record exactly which rows and which columns contain zeros. Then a single pass over each marked row and each marked column zeros them out in **O(M·N)** time and uses only **O(M+N)** extra space. This pattern—first find which rows and columns need to be zeroed, then zero them all in one go—keeps the solution simple and efficient.
