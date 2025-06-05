# brutforce approach

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        temp = []

        curr = head

        while curr:

            if curr in temp:
                return True
            
            temp.append(curr)
            curr = curr.next
        
        return False


# Optimal Approach (Floyd’s Cycle Detection Algorithm)


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        one = head # one step
        two = head # two steps 

        while two != None and two.next != None:

            one = one.next

            two = two.next.next

            if one == two:
                return True
            
        return False
        
