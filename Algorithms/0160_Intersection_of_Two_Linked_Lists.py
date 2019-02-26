# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if headA is None or headB is None:
            return None
        
        lengthA = lengthB = 0
        p = headA
        while p:
            lengthA += 1
            p = p.next
        
        p = headB
        while p:
            lengthB += 1
            p = p.next
            
        if lengthA < lengthB:
            headA, headB = headB, headA
            lengthA, lengthB = lengthB, lengthA
        
        gap = lengthA - lengthB
        while gap:
            headA = headA.next
            gap -= 1
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA
