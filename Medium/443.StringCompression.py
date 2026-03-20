#Link: https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0

        while read < len(chars):
            letter = chars[read]
            count = 0
            while read < len(chars) and chars[read] == letter:
                count += 1
                read += 1
            chars[write] = letter
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write
