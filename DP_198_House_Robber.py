# Reference: https://www.youtube.com/watch?v=73r3KWiEvyk&ab_channel=NeetCode
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        # [rob1], [rob2], n, n+1, n+2, ....
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
