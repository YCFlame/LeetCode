class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        def path(node):
            if not node:
                return 0
            
            left = right = 0
            if node.left:
                left = path(node.left) + 1
            if node.right:
                right = path(node.right) + 1
                        
            self.diameter = max(self.diameter, left + right)
            return max(left, right)
        
        path(root)
        return self.diameter
