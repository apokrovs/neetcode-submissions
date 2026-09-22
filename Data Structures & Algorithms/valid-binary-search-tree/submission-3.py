# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def isValid(node:Optional[TreeNode], low:int, high:int) -> bool:
            if low < node.val < high:
                left = True
                right = True
                if node.left:
                    left = isValid(node.left, low, node.val)
                if node.right:
                    right = isValid(node.right, node.val,high)
                return left and right
            else:
                return False
        return isValid(root, float('-inf'), float('inf'))


        