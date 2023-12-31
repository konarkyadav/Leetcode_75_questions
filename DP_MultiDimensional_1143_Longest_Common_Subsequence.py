# Reference: https://www.youtube.com/watch?v=y1b8pObvndA&ab_channel=CodeHelp-byBabbar
# https://www.youtube.com/watch?v=YL3b3F7sJBM&ab_channel=PrakashShukla
# https://www.youtube.com/watch?v=Ua0GhsJSlWM&ab_channel=NeetCode

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        # Base case: If either string is fully traversed
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]

        # def helper(text1, text2, i, j):
        #     # Base case: If either string is fully traversed
        #     if i == len(text1) or j == len(text2):
        #         return 0
            
        #     # If characters match, move to the next character in both strings
        #     if text1[i] == text2[j]:
        #         return 1 + helper(text1, text2, i + 1, j + 1)
        #     else:
        #         # If characters don't match, find the maximum by moving either in text1 or text2
        #         return max(helper(text1, text2, i, j + 1), helper(text1, text2, i + 1, j))
        
        # return helper(text1, text2, 0, 0)
