https://leetcode.com/problems/delete-node-in-a-linked-list/description/

## What I Learned

In this problem, I learned how to delete a node from a **singly linked list** when only that node is given, without access to the head of the list. 

Since we cannot access the previous node (which is usually needed to change the `.next` reference), we take a different approach:

- Copy the value from the **next node** into the current node.
- Update the current node's `.next` pointer to skip over the next node.

This effectively removes the next node and makes the current node take its place.

### 🔑 Key Takeaways
- Understanding how to **manipulate linked list pointers** in-place.
- Solving problems under **restricted access** (no head, no previous node).
- This solution only works when the node to delete is **not the tail node**, which is guaranteed by the problem.

### 🧪 Code Snippet

```python
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
