# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        result = []

        while queue:
            level = []
            while queue:
                q= queue.popleft()
                level.append(q)
            vals = []
            for l in level:
                vals.append(l.val)
                if l.left:
                    queue.append(l.left)
                if l.right:
                    queue.append(l.right)
            result.append(vals)
        return result
                
                
        