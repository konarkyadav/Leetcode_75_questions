# https://www.youtube.com/watch?v=9g1dV8UuYiM&ab_channel=EngineeringDigest
# https://www.youtube.com/watch?v=Y4SrfoquEpk&ab_channel=EngineeringDigest
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        answer = 0
        window = 0
        ans = 0
        n = len(nums)
        for right in range(len(nums)):
            window += nums[right]
            while (window + k < right - left + 1):
                window -= nums[left]
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans