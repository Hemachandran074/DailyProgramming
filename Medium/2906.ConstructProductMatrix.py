#Link: https://leetcode.com/problems/construct-product-matrix/

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        prod = 1
        n = len(grid)
        m = len(grid[0])

        ans = [[0] * m for _ in range(n)]

        prefix = 1
        for i in range(n):
            for j in range(m):
                ans[i][j] = prefix
                prefix = (ans[i][j] * grid[i][j]) % 12345

        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                ans[i][j] = (ans[i][j] * suffix) % 12345
                suffix = (suffix * grid[i][j]) % 12345

        return ans
