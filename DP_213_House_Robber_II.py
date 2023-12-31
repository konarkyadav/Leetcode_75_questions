class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        first = []
        second = []
        for i in range(len(nums)):
            if (i != len(nums) - 1):
                first.append(nums[i])
            if (i != 0):
                second.append(nums[i])
        def solve(nums):
            n = len(nums)
            prev2 = 0
            prev1 = nums[0]

            for i in range(1, n):
                incl = prev2 + nums[i]
                excl = prev1 + 0

                ans = max(incl, excl)
                prev2 = prev1
                prev1 = ans
            return prev1
        
        return max(solve(first), solve(second))


# Reference: https://www.youtube.com/watch?v=Fe2GeXEzWM0&t=608s&ab_channel=CodeHelp-byBabbar
# https://www.youtube.com/watch?v=m9-H6AUBLgY&ab_channel=CodeHelp-byBabbar