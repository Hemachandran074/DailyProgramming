#Link: https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        ans = [[0] * (m - k + 1) for _ in range(n - k + 1)]
        for i in range(n - k + 1):
            for j in range(m - k + 1):
                mat = [] 
                for row in range(i, i + k):
                    for col in range(j, j + k):
                        mat.append(grid[row][col])
                mat.sort()
            
                val = float('inf')
                for v in range(1, len(mat)):
                    if mat[v] != mat[v - 1]:
                        val = min(mat[v] - mat[v - 1], val)

                ans[i][j] = 0 if val == float('inf') else val
        return ans
