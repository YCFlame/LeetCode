# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = current = None
        def handle_node(node):
            nonlocal head, current
            if head is None:
                head = current = node
            else:
                current.next = node
                current = node
            
        while l1 and l2:
            if l1.val < l2.val:
                handle_node(l1)
                l1 = l1.next
            else:
                handle_node(l2)
                l2 = l2.next
                                
        if l1:
            handle_node(l1)
        else:
            handle_node(l2)
        
        return head
