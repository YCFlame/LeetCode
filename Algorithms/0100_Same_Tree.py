# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        from collections import deque
        queue = deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            if p and q:
                if p.val != q.val:
                    return False
                
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
            elif p != q:
                return False
        
        return True
