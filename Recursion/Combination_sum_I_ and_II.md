## What I Learned

### Combination Sum I
For this problem, I used a simple **recursive backtracking** with a **take-or-not-take** approach.  
Each number could be used unlimited times, so I called the recursive function without incrementing the index when I took the current number.  
This straightforward approach worked fine because we didn’t need to worry about duplicate combinations.

### Combination Sum II
Here, the challenge was handling **duplicates** and ensuring **unique combinations**.  
My initial take-or-not-take recursion created duplicate results and caused performance issues.  
To solve this:
- I **sorted** the input list.
- Switched to a **for-loop** recursion.
- Added a duplicate check (`if i > idx and candidates[i] == candidates[i-1]: continue`) at each level.

This optimization ensured we never picked the same number twice at the same recursion depth and drastically reduced unnecessary work.

