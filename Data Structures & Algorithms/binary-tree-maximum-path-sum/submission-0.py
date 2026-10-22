# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            path_sum = node.val + max([left, right, 0])
            self.res = max(self.res, node.val + max(left, 0) + max(right, 0))
            return path_sum

        dfs(root)
        return self.res