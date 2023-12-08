# This code is about depth first search
# Reference:  https://www.youtube.com/watch?v=7fm02dL9ZfM&ab_channel=ZackDo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(root):
    if not root:
        return []
    if not (root.left or root.right):
        return [root.val]
    return dfs(root.left) + dfs(root.right)

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return dfs(root1) == dfs(root2)