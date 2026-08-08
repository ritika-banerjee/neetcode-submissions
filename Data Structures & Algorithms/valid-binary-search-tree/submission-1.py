# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.prev = float('-inf')
        
        def inOrder(node):
            if not node:
                return True

            left = inOrder(node.left)
            if not left:
                return False

            if self.prev >= node.val:
                return False
                
            self.prev = node.val

            right = inOrder(node.right)
            if not right:
                return False

            return True

        return inOrder(root)
            

            