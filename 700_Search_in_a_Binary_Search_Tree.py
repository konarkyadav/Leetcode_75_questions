# Reference: https://www.youtube.com/watch?v=Lr2oxJlnLMM&ab_channel=Techdose
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def bst (node, val):
        if not node:
            return None
        if val > node.val:
            return bst(node.right, val)
        if val < node.val:
            return bst(node.left, val)
        else:
            return node
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return bst(root, val)