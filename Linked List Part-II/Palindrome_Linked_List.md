### What I Learned from “Palindrome Linked List” Problem

- **In-Place Reversal:**  
  Learned how to reverse a linked list iteratively by changing pointers, which is essential for many linked list problems.

- **Finding the Middle Node:**  
  Used slow and fast pointers to find the middle of the list efficiently in one pass, helping to split the list for palindrome checking.

- **Comparing Two Halves:**  
  After reversing the second half, compared values of nodes from the start and from the reversed part to check if the list is a palindrome without extra space.

- **Pointer Management:**  
  Understood the importance of careful pointer manipulation to avoid breaking the list structure or premature loop termination.

- **Optimal Time and Space Complexity:**  
  Implemented a solution that runs in O(n) time and O(1) extra space, which is the best possible for this problem.

- **Common Mistakes to Avoid:**  
  Learned that comparing nodes by value (not reference) is crucial, and ensuring loops fully traverse both halves before returning results is necessary to avoid wrong answers.

---

### How to Approach the Palindrome Linked List Problem

1. **Find the middle of the linked list:**  
   Use two pointers, slow and fast. Move slow by one step and fast by two steps until fast reaches the end. Slow will then be at the middle.

2. **Reverse the second half of the list:**  
   Starting from the middle node, reverse the pointers of the second half of the list.

3. **Compare the first half and the reversed second half:**  
   Move two pointers from the start of the list and the start of the reversed second half, comparing node values. If all values match, it is a palindrome.

4. **(Optional) Restore the original list structure:**  
   Reverse the second half again to restore the list if needed.

5. **Return the result:**  
   Return `True` if palindrome, otherwise `False`.

This approach ensures O(n) time complexity and O(1) extra space, making it efficient and optimal.
