### What I Learned from “Intersection of Two Linked Lists”

- **Node Comparison by Reference, Not Value:**  
  I learned that to find the intersection of two linked lists, I need to compare the actual node references, not just their values. Even if two nodes have the same value, they can be completely different nodes in memory.

- **Power of the Two-Pointer Technique:**  
  I used two pointers starting at the heads of both lists. When each pointer reaches the end of its list, I switch it to the head of the other list. This way, both pointers end up covering the same total distance. If there's an intersection, they’ll meet at that node. If not, they’ll meet at `None`.

- **Optimized Solution (Time & Space):**  
  This method works in O(m + n) time and uses only O(1) space. No need for extra data structures like hash sets — just smart pointer manipulation.

- **Clean Handling of Edge Cases:**  
  One thing I really liked about this approach is how naturally it handles the "no intersection" case. Both pointers just reach the end (`None`) at the same time without needing any special checks.
  
