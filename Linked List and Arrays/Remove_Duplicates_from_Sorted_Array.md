## What I Learned - Remove Duplicates from Sorted Array 

This problem taught me how to remove duplicates **in-place** from a sorted array using the **two-pointer technique**. Since the array is already sorted, all duplicates are next to each other, so it’s easy to compare adjacent elements.

### Key Takeaways:
- I used two pointers:
  - One (`i`) to iterate through the array
  - Another (`index`) to track where the next unique number should be placed
- Whenever I found a new unique number (`nums[i] != nums[i - 1]`), I placed it at `nums[index]` and incremented `index`
- At the end, `index` gives the count of unique elements, and the first `k` elements of the array hold those unique values in order

### Things I Learned:
- How to modify arrays without using extra space (`O(1)` space complexity)
- Why we can’t use a set or a new list when the problem specifically asks for an in-place solution
- How the two-pointer approach helps in many array-related problems, especially when dealing with sorted data
