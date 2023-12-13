class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        s = s.lower()
        finalCount = 0
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count+=1
        finalCount = count

        for i in range(k, len(s)):
            if s[i] in vowels:
                count+=1
            if s[i-k] in vowels:
                count -= 1
            finalCount = max(finalCount, count)
        return finalCount