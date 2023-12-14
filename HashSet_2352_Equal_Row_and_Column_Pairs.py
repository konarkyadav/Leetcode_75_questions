# References:
# https://www.youtube.com/watch?v=QWhQxJYppgo&ab_channel=codestorywithMIK
# https://medium.com/@kimyiyun302/2352-equal-row-and-column-pairs-beats-100-56fc51694ad2

from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows, cols = Counter(), Counter()
        n = len(grid)

        for i in range(n):
            rows[tuple(grid[i])] += 1
            cols[tuple(grid[r][i] for r in range(n))] += 1
        
        count = 0

        for key, val in rows.items():
            if key in cols:
                count += val * cols[key]
        return count