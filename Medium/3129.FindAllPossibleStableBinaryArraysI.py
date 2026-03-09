#Link: https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        
        def dp(z, o, last_placed):
            if z == 0 and o == 0:
                return 1
            
            if z < 0 or o < 0:
                return 0
                
            state = (z, o, last_placed)
            if state in memo:
                return memo[state]
            
            total_ways = 0

            if last_placed != 0:
                max_zeros_we_can_place = min(limit, z)
                for k in range(1, max_zeros_we_can_place + 1):
                    total_ways = (total_ways + dp(z - k, o, 0)) % MOD

            if last_placed != 1:
                max_ones_we_can_place = min(limit, o)
                for k in range(1, max_ones_we_can_place + 1):
                    total_ways = (total_ways + dp(z, o - k, 1)) % MOD

            memo[state] = total_ways
            return total_ways

        return dp(zero, one, -1)
