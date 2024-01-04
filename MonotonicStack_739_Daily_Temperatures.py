# Reference: https://www.youtube.com/watch?v=cTBiBSnjO3c&ab_channel=NeetCode
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer = [0] * len(temperatures)
#         for i in range(len(temperatures)):
#             for j in range(i + 1, len(temperatures)):
#                 if temperatures[i] < temperatures[j]:
#                     answer[i] = j - i
#                     break
#         return answer
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                value, index = stack.pop()
                answer[index] = (i - index)
            stack.append([t,i])
        return answer