#Link: https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = ""

        num = bin(n)[2:]
        length = len(num)

        mask = (2 ** length) - 1

        return n ^ mask
