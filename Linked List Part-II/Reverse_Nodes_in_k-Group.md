### Problem:
Given the head of a linked list, reverse the nodes in groups of size `k`.  
If the number of nodes is not a multiple of `k`, leave the remaining nodes as they are.

---

## What I learned from this problem:

- I understood how to reverse a linked list in groups without changing the values inside the nodes. Only the links between nodes are changed.
- I learned how using a dummy node makes it easier to handle edge cases, especially when the head node is part of the group that gets reversed.
- I learned that when working in `k` sized groups:
  - First I need to check if there are at least `k` nodes left.
  - Then reverse the nodes in that group using pointers.
- I got better at handling multiple pointers like `prev`, `curr`, and `next` while reversing the list.
- The head-insertion technique inside the group reversal was new to me, and now it makes more sense.
- I also learned how to handle edge cases like when `k = 1` or when the remaining nodes are less than `k`.

---

## Final Thoughts:

This problem helped me understand how to control a linked list better, especially when I need to modify it in place without using extra memory.

The logic I learned here will help me in other problems too, like rotating a list or reversing it in parts.
