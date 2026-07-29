# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self, root, max_depth, depth):
        if not root:
            return depth
        
        left_depth = self.recurse(root.left, max_depth, depth + 1)
        right_depth = self.recurse(root.right, max_depth, depth + 1)

        return left_depth if left_depth >= right_depth else right_depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root, 0, 0)