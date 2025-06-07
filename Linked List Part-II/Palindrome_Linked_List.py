# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head

        # this is for finding the middle value which at slow pointer
        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next
        

        # now we need to reverse the second half

        prev = None
        curr = slow

        while curr is not None:

            next = curr.next

            curr.next = prev

            prev = curr
            curr = next

        # now compare the first half with the second half

        first, second = head, prev

        while second is not None:

            if first.val != second.val:
                return False
            
            first = first.next
            second = second.next
        
        return True
        

