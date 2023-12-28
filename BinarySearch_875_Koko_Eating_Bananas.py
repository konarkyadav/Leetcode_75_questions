# Reference: https://www.youtube.com/watch?v=U2SozAs9RzA&ab_channel=NeetCode

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        res = right

        while left <= right:
            k = (left+right)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
        return res
