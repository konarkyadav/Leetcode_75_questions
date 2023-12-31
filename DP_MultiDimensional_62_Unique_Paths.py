# Reference: https://www.youtube.com/watch?v=x6R3OQCYmHo&ab_channel=PrakashShukla
# https://www.youtube.com/watch?v=DaakAKiCkyc&ab_channel=codestorywithMIK
# https://www.youtube.com/watch?v=IlEsdxuD4lY&ab_channel=NeetCode
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]

        for i in range(len(dp[0])):
            dp[0][i] = 1
        
        for i in range(len(dp)):
            dp[i][0] = 1
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]