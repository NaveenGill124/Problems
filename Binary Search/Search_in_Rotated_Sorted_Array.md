
## What I Learned from "Search in Rotated Sorted Array"

- I learned how to modify binary search to handle **rotated sorted arrays** where the sorted order is disrupted at some pivot.
- The key is to **determine which half (left or right) of the array is sorted** at each step, and then decide whether the target lies within that half.
- I realized that:
  - If `nums[low] <= nums[mid]`, then the **left half is sorted**.
  - If `nums[mid] <= nums[high]`, then the **right half is sorted**.
- One mistake I made was **returning -1 too early** if the target wasn't in the sorted half. I now understand that even if one side is sorted, the target might still be in the other half — so I should continue the binary search there.
- I also learned to be careful with **index boundaries**, especially with expressions like `nums[mid - 1]` and `nums[mid + 1]` — these can lead to **index out-of-bounds errors** if not handled properly.
- Most importantly, I reinforced the idea that binary search can be **adapted** beyond just searching sorted arrays — it's all about reducing the search space logically.

