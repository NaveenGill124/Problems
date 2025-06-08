# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        # count the number of nodes in the list
        count = 0
        while curr:
            count +=1
            curr = curr.next
            
        # reverse k nodes at a time

        while count >= k:

            curr = prev.next
            nxt = curr.next

            # reverse k nodes

            for i in range(1,k):

                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            
            prev = curr
            count -= k

        return dummy.next
