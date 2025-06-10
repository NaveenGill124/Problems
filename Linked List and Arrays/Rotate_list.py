# brute force approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head
        
        # for length

        length = 1
        curr = head
        while curr.next != None:
            
            curr = curr.next
            length += 1
        
        k = k % length

        if k == 0:
            return head
        

        for i in range(k):

            prev = None
            curr = head

            while curr.next != None:

                prev = curr
                curr = curr.next

            prev.next = None
            curr.next = head

            head = curr

        return head
        

#------------------------------Optimal approach with O(n) time complexity--------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head
        
        # for length

        length = 1
        curr = head
        while curr.next != None:
            
            curr = curr.next
            length += 1
        
        # Normalize k
        k = k % length
        if k == 0:
            return head

        # let's make list circular 
        curr.next = head
        
        # Find the new tail (length - k - 1 steps from head)
        steps_to_new_tail = length-k-1

        new_tail = head
        for i in range(steps_to_new_tail):
            
            new_tail = new_tail.next

        # Break the circle and set the new head
        new_head = new_tail.next
        new_tail.next = None

        return new_head
