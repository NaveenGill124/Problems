## What I Learned from This Problem

At first, I solved this problem using a **brute-force approach** by generating all possible permutations of numbers from `1` to `n`, sorting them, and then returning the k-th one. While this method worked for small values of `n`, it quickly became inefficient as `n` increased because the time complexity is **O(n!)**, which is not suitable for large inputs.

Later, I optimized my solution by using the **factorial number system**. I learned that we can calculate the k-th permutation directly without generating all permutations, by figuring out how many permutations exist for each starting digit. This method allowed me to build the final result step-by-step using simple division, modulo, and list operations.

###  Key Takeaways:
- How to solve a problem using both brute-force and optimized methods.
- The importance of analyzing time complexity and knowing when optimization is needed.
- Understanding the **factorial number system** and how it helps with indexing permutations.
- How to construct permutations directly without recursion or backtracking.

---

## Brute-Force Solution

```python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = []
        for i in range(1, n + 1):
            nums.append(i)

        result = []
        m = len(nums)

        def revert(nums, idx, result):
            if idx == m:
                result.append(nums[:])
                return
            for i in range(idx, m):
                nums[idx], nums[i] = nums[i], nums[idx]
                revert(nums, idx + 1, result)
                nums[idx], nums[i] = nums[i], nums[idx]

        revert(nums, 0, result)
        result.sort()
        final_output = result[k - 1]

        s = ''
        for i in final_output:
            s += str(i)

        return s
