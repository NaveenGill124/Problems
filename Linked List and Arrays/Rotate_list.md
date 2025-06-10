## 🔄 Rotate Linked List

#### Problem Statement

Given the head of a linked list, rotate the list to the right by `k` places.


---

### Approach

1. First, check for edge cases like empty list, one-node list, or `k == 0`.
2. Calculate the length of the linked list.
3. Use `k % length` to avoid unnecessary rotations.
4. Make the list circular by connecting the last node to the head.
5. Find the new tail by moving `(length - k - 1)` steps from the head.
6. Set the next node of `new_tail` as `new_head`, and break the circle by setting `new_tail.next = None`.

---

## What I Learned

While solving this problem, I learned:

- The importance of using `k % length` to avoid full unnecessary rotations.
- How to make a singly linked list temporarily circular (`tail.next = head`).
- How to locate the new tail of the list by stepping through `(length - k - 1)` nodes.
- That reassigning `.next` pointers actually changes the structure in memory — even if I stop using that variable.
- How to "break" a circular list correctly by doing `new_tail.next = None`.
- A useful visual way to understand it: imagine a train where the last car connects back to the engine, and you cut the loop at the right spot to rotate it.
- Clean coding habits like using meaningful variable names (`curr`, `new_tail`, `new_head`) and early returns.


