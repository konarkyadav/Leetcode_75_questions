# Reference:
# https://www.youtube.com/watch?v=nHMQ33LZ6oA&list=PLDzeHZWIZsTo87y1ytEAqp7wYlEP3nner&index=2&ab_channel=CodeHelp-byBabbar


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      if not root:
        return 0
      else:
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1