# https://www.youtube.com/watch?v=6jYxwdwjwKg&ab_channel=SaiAnishMalla
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         self.total = 0
#         self.lookup = defaultdict(int)
#         self.lookup[targetSum] = 1
#         def dfs(node, root_sum):
#             if not node:
#                 return
#             root_sum += node.val
#             self.total += self.lookup[root_sum]
#             self.lookup[root_sum+targetSum] += 1
#             dfs(node.left, root_sum)
#             dfs(node.right, root_sum)
#             self.lookup[root_sum+targetSum] -= 1
        
#         dfs(root,0)

#         return self.total

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(root, ps):
            if not root:
                return
            cs = ps + root.val
            x = cs - targetSum

            if (x in freq):
                self.count += freq[x]
            if cs in freq:
                freq[cs] += 1
            else:
                freq[cs] = 1
            
            dfs(root.left, cs)
            dfs(root.right, cs)
            freq[cs] -= 1

        
        self.count = 0
        freq = {0:1}
        dfs(root,0)
        return self.count