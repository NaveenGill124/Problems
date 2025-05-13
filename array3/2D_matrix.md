What I learned:
- A row-sorted matrix (with each row’s first element > previous row’s last) can be treated as a flat 1D array.
- Using `mid = (l+u)//2` and mapping back via `i = mid//n`, `j = mid%n` lets you do O(log(m·n)) binary search.
