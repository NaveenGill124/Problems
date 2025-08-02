# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # Copy the value from the next node to the current node
        node.val = node.next.val
        
        # Bypass the next node by linking current node to the next of next node
        node.next = node.next.next
