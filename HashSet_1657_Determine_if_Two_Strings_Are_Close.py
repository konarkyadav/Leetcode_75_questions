# https://dev.to/alvesjessica/leetcode-solution-determine-if-two-strings-are-close-3kb9
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = Counter(word1)
        dict2 = Counter(word2)
        return (len(word1) == len(word2) and set(dict1) == set(dict2) and 
        Counter(dict1.values()) == Counter(dict2.values()))