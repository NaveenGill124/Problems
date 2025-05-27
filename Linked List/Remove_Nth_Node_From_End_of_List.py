# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr1 = head
        count = 0
        while curr1 != None:
            count += 1
            curr1 = curr1.next

        if head == None or head.next == None:
            return None
        
        if count == n:
            return head.next
        
        curr = head
        for i in range(count-n-1):
            
            curr = curr.next
        
        if curr.next != None:

            curr.next = curr.next.next

        return head
