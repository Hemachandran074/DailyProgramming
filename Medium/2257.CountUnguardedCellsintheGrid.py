#Link: https://leetcode.com/problems/count-unguarded-cells-in-the-grid/


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        for row, col in guards:
            grid[row][col] = 1
        for row, col in walls:
            grid[row][col] = 2

        row = 0
        col = 0
        direction = [(-1, 0), (0, 1), (0, -1), (1, 0)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    for x, y in direction:
                        curr_row = x + row
                        curr_col = y + col
                        
                        while 0 <= curr_row < m and 0 <= curr_col < n:
                            if grid[curr_row][curr_col] in (1, 2):
                                break
                            if grid[curr_row][curr_col] == 0:
                                grid[curr_row][curr_col] = 3
                                
                            curr_row += x
                            curr_col += y

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    count += 1
        return count
