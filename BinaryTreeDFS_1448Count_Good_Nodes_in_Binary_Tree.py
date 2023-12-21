# https://www.youtube.com/watch?v=7cp5imvDzl4&ab_channel=NeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs (node, maxval):
            if not node:
                return 0
            else:
                if node.val >= maxval:
                    res = 1
                else:
                    res = 0
                maxval = max(maxval, node.val)
                res = res + dfs(node.left, maxval) + dfs(node.right, maxval)
                return res
        
        return dfs(root, root.val)
