# Reference: https://www.youtube.com/watch?v=NL1ocKYzlAM&ab_channel=Codebix
# Reference: https://www.youtube.com/watch?v=LFzAoJJt92M&ab_channel=NeetCodeIO

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if (key > root.val):
            root.right = self.deleteNode(root.right, key)
        elif (key < root.val):
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)
        return root