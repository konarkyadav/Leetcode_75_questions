class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
       set1, set2 = set(nums1), set(nums2)
       result1, result2 = set(), set()

       for n in nums1:
           if (n not in set2):
               result1.add(n)
       for n in nums2:
           if (n not in set1):
               result2.add(n)
       return [list(result1), list(result2)]