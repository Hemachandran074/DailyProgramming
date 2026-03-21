#Link: https://leetcode.com/problems/flip-square-submatrix-vertically/

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for row in range(x, x + k // 2):
            i = x + k - 1 - (row - x)
            for col in range(y, y + k):
                grid[row][col], grid[i][col] = grid[i][col], grid[row][col]
        
        return grid
