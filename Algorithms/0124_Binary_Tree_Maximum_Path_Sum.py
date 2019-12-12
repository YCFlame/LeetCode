# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        rs = float('-inf')
        def helper(node):
            if not node:
                return float('-inf')
            
            nonlocal rs
            res = node.val
            left = helper(node.left)
            if left > 0:
                res += left
            right = helper(node.right)
            if right > 0:
                res += right
            rs = max(rs, res)  # left and right themselves have been handled in their own recursive calls
            return max(left, right, 0) + node.val
        
        helper(root)
        return rs
