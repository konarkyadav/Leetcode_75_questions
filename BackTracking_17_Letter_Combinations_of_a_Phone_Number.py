# Reference: https://www.youtube.com/watch?v=0snEunUacZY&ab_channel=NeetCode
# Reference: https://www.youtube.com/watch?v=tWnHbSHwNmA&ab_channel=CodeHelp-byBabbar
# https://www.youtube.com/watch?v=8orpUBZZ9l0&ab_channel=PrakashShukla
# https://www.youtube.com/watch?v=vgnhZzw-kfU&ab_channel=codestorywithMIK
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dictionary = {"2": "abc",
                      "3": "def",
                      "4": "ghi",
                      "5": "jkl",
                      "6": "mno",
                      "7": "pqrs",
                      "8": "tuv",
                      "9": "wxyz"}
        
        def helper(i, currstr):
            if (len(currstr) == len(digits)):
                res.append(currstr)
                return
            for c in dictionary[digits[i]]:
                helper(i+1, currstr+c)
        if digits:
            helper(0, "")
        return res
