# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        curr = head
        curr1 = head
        count = 0
      
        while curr != None:

            count += 1

            curr = curr.next

        n = count//2
        
        for i in range(n):

            curr1 = curr1.next

        return curr1
