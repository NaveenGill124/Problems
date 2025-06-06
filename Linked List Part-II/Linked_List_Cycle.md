## 🧠 What I Learned

- Learned how to detect cycles in a linked list using different approaches.
- Understood that `if node in visited` compares node references, not values.
- Improved the brute-force approach using a `set` for faster O(1) lookup time.
- Implemented Floyd’s Cycle Detection Algorithm (Tortoise and Hare) using two pointers moving at different speeds (1 and 2 steps). This method detects cycles efficiently with O(1) space and O(n) time.
- Explored why we specifically use (1, 2) step movement. Although combinations like (1, 3), (1, 4), or (2, 3) are possible, (1, 2) is optimal because it guarantees a consistent 1-step difference, ensuring the pointers meet inside a cycle.
- Gained a better understanding of pointers, object identity, and space-time optimization in linked list problems.
