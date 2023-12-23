# Reference: https://www.youtube.com/watch?v=s1d8UGDCCN8&t=3634s&ab_channel=CodeHelp-byBabbar

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def solve(root: Optional[TreeNode], ans, level):
            if not root:
                return
            if (level == len(ans)):
                ans.append(root.val)
            solve(root.right, ans, level+1)
            solve(root.left, ans, level+1) 
        
        ans = []
        solve(root, ans, 0)
        return ans