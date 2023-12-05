import sys


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = 0
        windowSumValue = 0
        answer = -sys.maxsize - 1
        while (right < len(nums)):
            if ((right - left) < k):
                windowSumValue += nums[right]
                right += 1
            elif ((right - left) == k):
                answer = max(answer, windowSumValue)
                windowSumValue = windowSumValue + nums[right]
                right += 1
                windowSumValue = windowSumValue - nums[left]
                left += 1
        
        answer = max(answer, windowSumValue)
        return answer/k