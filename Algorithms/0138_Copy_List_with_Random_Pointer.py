"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        p = head
        while p:
            q = Node(p.val, p.next, None)
            p.next = q
            p = q.next
        
        p = head
        while p:
            p.next.random = p.random.next if p.random else None
            p = p.next.next
        
        old = head
        new = head.next
        res = new
        while old:
        """
        can't handle random pointers here because old nodes have been unweaved,
        which means old.random.next won't point to new nodes
        """
            old.next = new.next
            new.next = old.next.next if old.next else None
            old = old.next
            new = new.next
        
        return res
            
