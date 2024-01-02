# Reference: https://www.youtube.com/watch?v=dlKGCNVel6A&t=37s&ab_channel=CodeHelp-byBabbar

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         def helper(index, buy, prices):
#             if index == len(prices):
#                 return 0
#             if buy:
#                 profit = max((-prices[index] + helper(index+1, 0, prices)), (0 + helper(index+1, 1, prices)))
#             else:
#                 profit = max((prices[index]+ helper(index+1, 1, prices)), (0 + helper(index+1, 0, prices)))
#             return profit
#         return helper(0, 1, prices)



# Iterate on array from 1 to n. Wherever, arr[i] > arr[i-1], add it to profit.

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#     	profit = 0
#     	for i in range(1, len(prices)):
#     		if prices[i] > prices[i-1]:
#     			profit += prices[i] - prices[i-1]
#     	return profit


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         dp = [[-1 for _ in range(2)] for _ in range(len(prices))]

#         def helper(index, buy, prices, dp):
#             if index == len(prices):
#                 return 0
#             if dp[index][buy] != -1:
#                 return dp[index][buy]
#             if buy:
#                 profit = max((-prices[index] + helper(index+1, 0, prices, dp)), (0 + helper(index+1, 1, prices, dp)))
#             else:
#                 profit = max((prices[index]+ helper(index+1, 1, prices, dp)), (0 + helper(index+1, 0, prices, dp)))
#             dp[index][buy] = profit
#             return dp[index][buy]
#         return helper(0, 1, prices, dp)

# Bottom's up
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        dp = [[-1 for _ in range(2)] for _ in range(len(prices))]

        def helper(index, buy, prices, dp):
            if index == len(prices):
                return 0
            if dp[index][buy] != -1:
                return dp[index][buy]
            if buy:
                profit = max((-prices[index] + helper(index+1, 0, prices, dp)), (0 + helper(index+1, 1, prices, dp)))
            else:
                profit = max((prices[index]+ helper(index+1, 1, prices, dp)), (0 + helper(index+1, 0, prices, dp)))
            dp[index][buy] = profit
            return dp[index][buy]
        return helper(0, 1, prices, dp)

