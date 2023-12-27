# Reference: https://www.youtube.com/watch?v=OKnm5oyAhWg&ab_channel=NeetCodeIO

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []

        for s in spells:
            left = 0
            right = len(potions) - 1
            index = len(potions)
            while (left <= right):
                middle = (left+right)//2
                if s*potions[middle] >= success:
                    right = middle - 1
                    index = middle
                else:
                    left = middle + 1

            res.append(len(potions) - index)
        return res