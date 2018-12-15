# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        prev = head
        current = head.next
        while current is not None:
            while current and prev.val == current.val:
                current = current.next
            
            prev.next = current
            prev = current    
            
        return head
