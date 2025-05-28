# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)

        temp = dummy

        carry = 0

        while l1 != None or l2 != None:

            sum = carry

            if l1 != None:

                sum = sum + l1.val

                l1 = l1.next
            
            if l2 != None:

                sum = sum + l2.val

                l2 = l2.next
            

            carry = sum // 10

            temp.next = ListNode(sum % 10)

            temp = temp.next
        
        if carry > 0:
            temp.next = ListNode(carry)

        return dummy.next

