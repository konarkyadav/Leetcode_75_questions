class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        l1 = len(word1)
        l2 = len(word2)
        i = 0
        while (i < l1 or i < l2):
            if (i < l1):
                answer += word1[i]
            if (i < l2):
                answer += word2[i]
            i+=1
        return answer