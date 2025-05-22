## What I Learned

- How to reverse a linked list by changing the direction of `next` pointers.
- Used three pointers: `prev`, `curr`, and `next_node` to iterate and reverse the list.
- This improved my understanding of pointer manipulation and iterative traversal in linked lists.

### Approach
1. Initialize `prev = None` and `curr = head`.
2. Loop through the list:
   - Save `curr.next` in `next_node`.
   - Point `curr.next` to `prev`.
   - Move `prev` and `curr` one step forward.
3. After the loop, return `prev` as the new head of the reversed list.

#### Code
```python
def reverseList(head):
    prev = None
    curr = head

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev
