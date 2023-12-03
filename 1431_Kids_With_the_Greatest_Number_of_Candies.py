class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = -1
        for i in candies:
            if (i > maximum):
                maximum = i
        result = []
        for i in candies:
            if ((i + extraCandies) >= maximum):
                result.append(True)
            else:
                result.append(False)
        
        return result