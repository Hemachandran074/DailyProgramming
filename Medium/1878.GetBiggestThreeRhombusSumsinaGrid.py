#Link: https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        sums = set()
        m = len(grid)
        n = len(grid[0])

        for r in range(m):
            for c in range(n):
                L = 0

                while c - L >= 0 and c + L < n and r + 2 * L < m:
                    if L == 0:
                        sums.add(grid[r][c])
                    else:
                        current_sum = 0
                        curr_r = r
                        curr_c = c
                        for _ in range(L):
                            curr_r += 1
                            curr_c += 1
                            current_sum = current_sum + grid[curr_r][curr_c]
                        for _ in range(L):
                            curr_r += 1
                            curr_c -= 1
                            current_sum = current_sum + grid[curr_r][curr_c]
                        for _ in range(L):
                            curr_r -= 1
                            curr_c -= 1
                            current_sum = current_sum + grid[curr_r][curr_c]
                        for _ in range(L):
                            curr_r -= 1
                            curr_c += 1
                            current_sum = current_sum + grid[curr_r][curr_c]
                        
                        sums.add(current_sum)
                    L += 1
        sorted_sums = sorted(list(sums), reverse = True)
        return sorted_sums[:3]
