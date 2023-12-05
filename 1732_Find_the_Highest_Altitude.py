class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maximum_height = 0
        current = 0
        for i in range(0,len(gain)):
            current += gain[i]
            maximum_height = max(maximum_height, current)
        return maximum_height