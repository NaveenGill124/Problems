### What I learned with two Sum problem
- Started with a brute-force O(n²) approach, then refactored to an O(n) solution using a hash map to track seen numbers and their indices.  
- For each `num`, compute `comp = target - num`, check the map in O(1), and store `num` if not found.

