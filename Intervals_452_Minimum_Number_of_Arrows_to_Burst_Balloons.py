# Reference: https://www.youtube.com/watch?v=_WIFehFkkig&ab_channel=TimothyHChang
# https://walkccc.me/LeetCode/problems/0452/#__tabbed_1_3
# class Solution:
#     def findMinArrowShots(self, points: List[List[int]]) -> int:
#         points.sort()
#         prev = points[0]
#         total = 1
#         for s,e in points[1:]:
#             if s > prev[1]:
#                 total += 1
#                 prev = [s,e]
#             else:
#                 prev[1] = min(prev[1], e)
#         return total

class Solution:
  def findMinArrowShots(self, points: List[List[int]]) -> int:
    ans = 0
    arrowX = -math.inf

    for point in sorted(points, key=lambda x: x[1]):
      if point[0] > arrowX:
        ans += 1
        arrowX = point[1]

    return ans
