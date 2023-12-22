# reference: https://www.youtube.com/watch?v=bAO794rh_4M&t=464s&ab_channel=codestorywithMIK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxPath = 0
    def dfs(self, root: Optional [TreeNode], steps, goleft):
        if not root:
            return
        self.maxPath = max(self.maxPath, steps)
        if (goleft == True):
            self.dfs(root.left, steps+1, False)
            self.dfs(root.right, 1, True)
        else:
            self.dfs(root.right, steps+1, True)
            self.dfs(root.left, 1, False)


    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0, True)
        self.dfs(root, 0, False)
        return self.maxPath