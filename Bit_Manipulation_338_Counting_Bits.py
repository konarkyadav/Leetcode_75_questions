class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range (0,n+1):
            ans.append(num.bit_count())
        return ans