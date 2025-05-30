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

### Next Permutation
- In solving “Next Permutation,” I learned to break the problem into clear steps—identifying the pivot, swapping with the next larger element, and reversing the suffix—to systematically generate the next lexicographical order.  
- Along the way, I refreshed key Python techniques like reverse loops, in-place swaps, and efficient slice operations.  


### Sort Colors Problem
- While the built-in `nums.sort()` one-liner is concise, it runs in O(n log n) time; the Dutch National Flag algorithm partitions the three colors in a single pass (O(n) time, O(1) space), making it far more efficient for this problem.  
- This shows that brevity in code doesn’t always equate to optimal performance—sometimes a few extra lines unlock significant time savings.  
