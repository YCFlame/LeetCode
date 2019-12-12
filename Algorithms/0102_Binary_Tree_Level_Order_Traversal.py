from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        rs = []
        q = deque([root])
        while q:
            length = len(q)
            tmp = []
            for i in range(length):
                n = q.popleft()
                tmp.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)                
            
            rs.append(tmp)
                
        return rs           
