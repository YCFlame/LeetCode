# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p = q = dummy
        for i in range(n + 1):
            q = q.next
        
        while q is not None:
            p = p.next
            q = q.next

        p.next = p.next.next
        return dummy.next
