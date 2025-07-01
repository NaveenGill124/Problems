## What I learned from the problem "Single Element in a Sorted Array" Using Binary Search

---

### 1. Importance of Edge Case Handling
Initially, I didn't consider edge cases where the single element could be at the **start or end** of the array. This led to incorrect results or index out-of-bounds errors. After debugging, I learned to:
- Check explicitly if `mid == 0` or `mid == len(nums) - 1`
- Compare carefully with neighbors before making any assumptions

### 2. Use of Mid Index and Even/Odd Behavior
At first, I didn’t think about using `mid % 2` to determine which side of the array to continue searching. But eventually, I understood that:
- In a correctly paired array, the **first instance** of a pair is always at an **even index**
- If this pattern breaks, the single element lies **before** that index

### 3. Binary Search with Pairs Has Unique Patterns
Unlike standard binary search, here the key was to detect patterns in pairs:
- If `mid` is even and `nums[mid] == nums[mid + 1]`, we search the right
- If not, the unique element lies on the left

### 4. Writing Cleaner and Commented Code
After getting it wrong a few times, I also learned the importance of:
- Writing clear comments for logic branches
- Structuring binary search problems step-by-step
