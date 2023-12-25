# Reference: https://www.youtube.com/watch?v=XEmy13g1Qxc&ab_channel=NeetCode

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]

# import heapq
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heapq.heapify(nums)
#         return heapq.nlargest(k, nums)[-1]

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         k = len(nums) - k
        
#         def quicksort(l,r):
#             pivot, p = nums[r], l
#             for i in range(l,r):
#                 if nums[i] <= pivot:
#                     nums[p], nums[i] = nums[i], nums[p]
#                     p+=1
#             nums[p], nums[r] = nums[r], nums[p]

#             if k < p:
#                 return quicksort(l, p-1)
#             elif k > p:
#                 return quicksort(p+1, r)
#             else:
#                 return nums[p]
#         return quicksort(0, len(nums)-1)