## What I Learned

### Maximum_Subarray
I learned about **Kadane's Algorithm** and how it efficiently solves the Maximum Subarray problem in **O(n)** time complexity. 

Before discovering Kadane’s approach, I attempted solutions using brute force and nested loops, which resulted in **O(n²)** or even **O(n³)** time complexity. These approaches were not optimal for large inputs and led to performance issues.

Kadane's Algorithm offers a much better and elegant solution by iterating through the array once and dynamically tracking the maximum subarray sum. It's a great example of how a greedy approach can drastically improve efficiency in certain problems.

This was a valuable learning experience in understanding both **algorithm optimization** and **time complexity analysis**.


### Stock Buy and Sell

I learned that to solve the stock profit problem, we only need to keep track of the minimum stock price so far and calculate the maximum profit by comparing the current day's price with that minimum. This allows us to find the best time to buy and sell in a single pass through the list.

