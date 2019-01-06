# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            start, end = 0, len(queue) - 1
            while start < end:
                p, q = queue[start], queue[end]
                if p and q:
                    if p.val != q.val:
                        return False
                elif p or q:
                    return False
                start += 1
                end -= 1
            tmp = []
            for i in queue:
                if i is not None:
                    tmp.append(i.left)
                    tmp.append(i.right)
            queue = tmp
            
        return True
