#Link: https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        count = 0

        for r in range(m):
            for c in range(n):
                prefix[r + 1][c + 1] = prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c] + grid[r][c]
                if prefix[r + 1][c + 1] <= k:
                    count += 1
        
        return count
