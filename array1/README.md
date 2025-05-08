## What I Learned

### Maximum_Subarray
I learned about **Kadane's Algorithm** and how it efficiently solves the Maximum Subarray problem in **O(n)** time complexity. 

Before discovering Kadane’s approach, I attempted solutions using brute force and nested loops, which resulted in **O(n²)** or even **O(n³)** time complexity. These approaches were not optimal for large inputs and led to performance issues.

Kadane's Algorithm offers a much better and elegant solution by iterating through the array once and dynamically tracking the maximum subarray sum. It's a great example of how a greedy approach can drastically improve efficiency in certain problems.

This was a valuable learning experience in understanding both **algorithm optimization** and **time complexity analysis**.


### Stock Buy and Sell

I learned that to solve the stock profit problem, we only need to keep track of the minimum stock price so far and calculate the maximum profit by comparing the current day's price with that minimum. This allows us to find the best time to buy and sell in a single pass through the list.

### Set Matrix Zeros

When solving the “Set Matrix Zeroes” problem, it’s tempting to jump straight into a brute-force solution, but stepping back to analyze the optimal approach really pays off. Instead of zeroing out rows and columns repeatedly for every zero found (which can cost **O(M·N·(M+N))** time in the worst case), we scan the matrix once to record exactly which rows and which columns contain zeros. Then a single pass over each marked row and each marked column zeros them out in **O(M·N)** time and uses only **O(M+N)** extra space. This pattern—first find which rows and columns need to be zeroed, then zero them all in one go—keeps the solution simple and efficient.

### Pascal's Triangle

