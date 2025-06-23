## What I Learned

### What I learned from the **Subset** problem:
- I practiced the basic **backtracking** pattern — at each index, I either include the number or skip it.
- I learned how recursion explores all possible subsets by going one level deeper and then backtracking (`append()` then `pop()`) to try a different path.
- The **base case** (`i == len(nums)`) was super important because that’s where I add the current path to the result.
- This really helped me understand how recursion walks through all the combinations like a tree — going left (skip) and right (include) at every element.

---

### What I learned from the **Subset II** problem:
- Here I had to **handle duplicates**, so the first thing I did was sort the list — this way the duplicate numbers are next to each other.
- Even then, just backtracking gave me duplicate subsets. To fix that, I put my subsets into a **set of tuples** so only unique ones remain.
- Finally, I converted those tuples back into lists before returning.
- Going through this also made recursion click even more — I could clearly see that we’re making decisions at each element and using backtracking to cover all options without missing any.

