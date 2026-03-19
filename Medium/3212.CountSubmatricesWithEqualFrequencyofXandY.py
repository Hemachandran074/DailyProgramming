#Link: https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        prefix_x = [[0] * (m + 1) for _ in range(n + 1)]
        prefix_y = [[0] * (m + 1) for _ in range(n + 1)]
        count = 0

        for r in range(n):
            for c in range(m):
                val_x = 1 if grid[r][c] == "X" else 0
                val_y = 1 if grid[r][c] == "Y" else 0

                prefix_x[r + 1][c + 1] = prefix_x[r][c + 1] + prefix_x[r + 1][c] - prefix_x[r][c] + val_x
                prefix_y[r + 1][c + 1] = prefix_y[r][c + 1] + prefix_y[r + 1][c] - prefix_y[r][c] + val_y
                current_X = prefix_x[r + 1][c + 1]
                current_Y = prefix_y[r + 1][c + 1]
                
                if current_X == current_Y and current_X >= 1:
                    count += 1
        return count
