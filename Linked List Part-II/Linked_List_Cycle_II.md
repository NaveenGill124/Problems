## What I Learned

Working through this problem taught me a lot about pointer techniques and elegant algorithm design:

- I saw first-hand how the two-pointer (or “tortoise and hare”) trick can detect a cycle in a single pass through the list, keeping time complexity to O(n) and using absolutely no extra space beyond the pointers themselves.
- I gained an appreciation for the math behind finding the exact entry point of the loop. By resetting one pointer back to the head and moving both pointers one step at a time, they’re guaranteed to meet right where the cycle begins.
- Handling edge cases became second nature—I now know how to gracefully handle an empty list, a one-node list that loops to itself, and even larger lists where the cycle jumps back to the head.
- Breaking the logic into “detection” and “entry-location” phases, choosing clear variable names (`slow`, `fast`, `entry`), and adding concise comments makes the solution easy to follow and maintain.

---

### My Implementation in Two Phases

1. **Detection Phase**  
   I start with two pointers at the head: `slow` moves one node at a time, `fast` moves two. If there’s a cycle, they’ll eventually collide.

2. **Locating the Cycle Start**  
   As soon as `slow` meets `fast`, I introduce a third pointer (I call it `entry`) at the head. Moving both `slow` and `entry` one step at a time brings them together exactly at the node where the cycle begins.

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = entry = head

        # Phase 1: find collision
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Phase 2: find cycle start
                while slow != entry:
                    slow = slow.next
                    entry = entry.next
                return entry

        return None
