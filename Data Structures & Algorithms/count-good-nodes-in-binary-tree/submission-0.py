# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        maximum = float('-inf')

        def get_max_count(node, maximum):
            if not node:
                return

            if node.val >= maximum:
                maximum = node.val
                self.count += 1

            get_max_count(node.left, maximum)
            get_max_count(node.right, maximum)

        get_max_count(root, maximum)
        return self.count