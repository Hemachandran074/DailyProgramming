# Link: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        happy = ["a", "b", "c"]
        result = []

        def backtrack(letter):
            if len(result) == k:
                return

            if len(letter) == n:
                result.append(letter)
                return

            for i in happy:
                if not letter or letter[-1] != i:
                    backtrack(letter + i)

        backtrack("")
        return result[-1] if len(result) == k else ""
