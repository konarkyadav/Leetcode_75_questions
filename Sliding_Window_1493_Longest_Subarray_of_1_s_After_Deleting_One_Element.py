# https://medium.com/@entrustech/longest-subarray-of-1s-after-deleting-one-element-174f6c902cba
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = zeroCount = maxLen = 0
        while (right < len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            while (zeroCount > 1):
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            maxLen = max(maxLen, right - left)
            right += 1
        return maxLen