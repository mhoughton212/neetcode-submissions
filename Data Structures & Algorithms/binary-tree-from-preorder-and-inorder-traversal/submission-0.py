# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = {val: i for i, val in enumerate(inorder)}
        self.idx = 0
        def dfs(l, r):
            if l > r:
                return
            node = TreeNode(preorder[self.idx])
            self.idx += 1
            inorder_idx = inorder_indices[node.val]
            node.left = dfs(l, inorder_idx - 1)
            node.right = dfs(inorder_idx + 1, r)
            return node

        return dfs(0, len(inorder) - 1)