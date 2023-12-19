# Reference: https://www.youtube.com/watch?v=qB0zZpBJlh8&t=878&ab_channel=NeetCode
class Solution:
    def decodeString(self, s: str) -> str:
        answer = []
        for i in range(len(s)):
            if s[i] != "]":
                answer.append(s[i])
            else:
                substr = ""
                while answer[-1] != "[":
                    substr = answer.pop() + substr
                answer.pop()

                k = ""
                while answer and answer[-1].isdigit():
                    k = answer.pop() + k
                answer.append(int(k) * substr)
        return "".join(answer)