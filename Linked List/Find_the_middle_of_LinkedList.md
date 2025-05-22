## What I Learned

### Find the Middle of a Linked List


I learned how to find the middle node of a singly linked list by **counting the total number of nodes** and then moving to the middle index. This is a straightforward and easy-to-understand approach, though it requires two passes through the list.

### Key Concepts

- First, traverse the entire list to count the number of nodes.
- Divide the count by 2 to get the index of the middle node.
- Traverse the list again up to the middle index and return that node.
- If the number of nodes is even, it returns the **second middle** node, as required.

### Example

For a list like:  
`1 → 2 → 3 → 4 → 5 → 6`  
Total nodes = 6 → `6 // 2 = 3`  
After 3 steps from head, we reach node `4`, which is the **second middle node**.

### Code

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        curr1 = head
        count = 0

        # First pass to count nodes
        while curr:
            count += 1
            curr = curr.next

        # Second pass to reach middle node
        for _ in range(count // 2):
            curr1 = curr1.next

        return curr1
