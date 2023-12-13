# https://www.youtube.com/watch?v=UuiTKBwPgAo&ab_channel=NeetCode
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while (left < right):
            area = (right - left) * min (height[right], height[left])
            maxArea = max(maxArea, area)

            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return maxArea