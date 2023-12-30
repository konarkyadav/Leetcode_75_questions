# Reference: https://www.youtube.com/watch?v=Iwmn-gFL3c0&ab_channel=codestorywithMIK
# https://www.youtube.com/watch?v=RhhCWPGsJ0I&ab_channel=EliteCode

# Formula: F(n) = 2*F(N-1) + F(N-3)
class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (n+1)
        if n < 3:
            return n
        if n == 3:
            return 5
        else:
            dp[0], dp[1], dp[2], dp[3] = 0,1,2,5
            for i in range(4, n+1):
                dp[i] = (2*dp[i-1]%mod + dp[i-3]%mod)%mod
            return dp[n]
