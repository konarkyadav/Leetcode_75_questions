# Reference: https://www.youtube.com/watch?v=J2hcPZRpbMk&ab_channel=SaiAnishMalla

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack (nums, stack, target):
            if len(stack) == k:
                if target == 0:
                    res.append(stack)
            
            for i in range(nums+1, 10):
                if i <= target:
                    backtrack(i, stack + [i], target - i)
                else:
                    return
        backtrack(0, [], n)
        return res
        # all_combs = list(itertools.combinations(list(range(1,10)), k))
        # return [a for a in all_combs if sum(a) == n]