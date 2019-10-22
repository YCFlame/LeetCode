# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = l1
        cur = dummy
        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            cur.next = l1
            cur = l1
            l1 = l1.next
        
        cur.next = l1 if l1 else l2 
        
        return dummy.next
