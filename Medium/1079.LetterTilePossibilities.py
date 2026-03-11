#Link: https://leetcode.com/problems/letter-tile-possibilities/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        table = Counter(tiles)
        tiles_set = set(tiles)
        
        def backtrack():
            count = 0

            for i in tiles_set:
                if table[i] > 0:
                    count += 1
                    table[i] -= 1
                    count += backtrack()
                    table[i] += 1
            return count

        return backtrack()
