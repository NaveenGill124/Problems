## ⛰️ What I Learned from "Peak Index in a Mountain Array"

- This problem helped me understand how to apply **binary search** in a slightly different way — not just for finding a number, but for finding a **peak element**.
- I realized early on that one side of the peak is **strictly increasing** and the other side is **strictly decreasing**, which is key to using binary search efficiently.
- The tricky part where I got stuck was setting the initial bounds:
 ```python
  low = 1
  high = len(arr) - 2
```
- I use `low = 1` and `high = len(arr) - 2` instead of `0` and `len(arr) - 1` because the peak is guaranteed not to be at the ends, and we need to safely access both `arr[mid - 1]` and `arr[mid + 1]` during comparisons without causing index-out-of-range errors.
- I learned how to write cleaner logic by checking:
  - If `arr[mid] > arr[mid - 1]`, I’m still on the increasing side → move right.
  - Else, I’m on the decreasing side → move left.
- Overall, I learned that binary search is not just for sorted arrays — it can be **adapted to problems with structure**, like this one, as long as I understand how to move the bounds logically.


