#Link: https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[0, 0] for _ in range(m)] for _ in range(n)]
        dp[0][0] = [grid[0][0], grid[0][0]]

        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0:
                    p1 = dp[i - 1][j][0] * grid[i][j]
                    p2 = dp[i - 1][j][1] * grid[i][j]
                    p3 = dp[i][j - 1][0] * grid[i][j]
                    p4 = dp[i][j - 1][1] * grid[i][j]
                    
                    dp[i][j][0] = min(p1, p2, p3, p4)
                    dp[i][j][1] = max(p1, p2, p3, p4)
                elif i > 0:
                    p1 = dp[i - 1][j][0] * grid[i][j]
                    p2 = dp[i - 1][j][1] * grid[i][j]
                    dp[i][j][0] = min(p1, p2)
                    dp[i][j][1] = max(p1, p2)
                elif j > 0:
                    p3 = dp[i][j - 1][0] * grid[i][j]
                    p4 = dp[i][j - 1][1] * grid[i][j]
                    dp[i][j][0] = min(p3, p4)
                    dp[i][j][1] = max(p3, p4)

        if dp[n - 1][m - 1][1] >= 0:
            return (dp[n - 1][m - 1][1]) % ((10 ** 9) + 7)
        return -1
