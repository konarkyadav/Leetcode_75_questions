# class Solution:
#     def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
#         N = len(costs)
#         h = []

#         left = 0
#         right = N-1

#         for i in range(candidates):
#             heapq.heappush(h, (costs[left], left, 1))
#             left += 1
        
#         for i in range(candidates):
#             if left >= right:
#                 break
#             heapq.heappush(h, (costs[right], right, -1))
#             right -= 1
        
#         total = 0
#         for index in range(k):
#             cost, index, left_right_direction = heapq.heappop(h)

#             total += cost
#             if left <= right:
#                 if left_right_direction == 1:
#                     heapq.heappush(h, (costs[left], left, 1))
#                     left += 1
#                 else:
#                     heapq.heappush(h, (costs[right], right, -1))
#                     right -= 1
#         return total

import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs)
        h = []

        left = 0
        right = N - 1

        for i in range(candidates):
            heapq.heappush(h, (costs[left], left, 1))
            left += 1
        
        for i in range(candidates):
            if left > right:
                break
            heapq.heappush(h, (costs[right], right, -1))
            right -= 1
        
        total = 0
        for _ in range(k):
            cost, index, left_right_direction = heapq.heappop(h)

            total += cost
            if left_right_direction == 1 and left <= right:
                heapq.heappush(h, (costs[left], left, 1))
                left += 1
            elif left_right_direction == -1 and left <= right:
                heapq.heappush(h, (costs[right], right, -1))
                right -= 1

        return total
