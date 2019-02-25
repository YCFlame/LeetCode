# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p, q = None, head
        while q is not None:
            if q.val == val:
                if p is None:
                    head = q.next
                    q.next = None
                    q = head
                else:
                    p.next = q.next
                    q.next = None
                    q = p.next
            else:
                p = q
                q = q.next
                
        return head
        
 """
 class Solution:
    def removeElements(self, head: 'ListNode', val: 'int') -> 'ListNode':
        if not head:
            return None
        
        current = head
        
        while current.next:
            
            if current.next.val == val:
                current.next = current.next.next
            
            else:
                current = current.next
                
        return head.next if head.val == val else head
 """
