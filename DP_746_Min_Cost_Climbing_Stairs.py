# https://www.youtube.com/watch?v=S31W3kohFDk&t=1616s&ab_channel=CodeHelp-byBabbar

# class Solution:
#     def solve(self, cost, n):
#         # Base case
#         if (n==0 or n==1):
#             return cost[n]

#         return cost[n] + min(self.solve(cost, n-1), self.solve(cost, n-2))

#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         return min(self.solve(cost, n-1), self.solve(cost, n-2))

class Solution:
    def solve(self, cost, n, dp):
        # Base case
        if (n==0 or n==1):
            return cost[n]
        if (dp[n] != -1):
            return dp[n]

        dp[n] = cost[n] + min(self.solve(cost, n-1, dp), self.solve(cost, n-2, dp))
        return dp[n]

    def solve2(self, cost, n):
        dp = [-1] * (n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[n-1], dp[n-2])
    
    def solve3(self, cost, n):
        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2,n):
            curr = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr
        
        return min(prev1, prev2)



    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # dp = [-1] * (n+1)
        # return min(self.solve(cost, n-1, dp), self.solve(cost, n-2, dp))
        n = len(cost)
        # return self.solve2(cost, n)
        return self.solve3(cost, n)
