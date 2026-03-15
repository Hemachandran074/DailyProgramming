# Link: https://leetcode.com/problems/fancy-sequence/

class Fancy:
    MOD = (10 ** 9) + 7
    def __init__(self):
        self.nums = []
        self.multiplier = 1
        self.increment = 0

    def append(self, val: int) -> None:
        x = ((val - self.increment) * pow(self.multiplier, -1, self.MOD)) % self.MOD
        self.nums.append(x)

    def addAll(self, inc: int) -> None:
        if not self.nums:
            return
        self.increment = (self.increment + inc) % self.MOD

    def multAll(self, m: int) -> None:
        if not self.nums:
            return
        self.multiplier = (self.multiplier * m) % self.MOD
        self.increment = (self.increment * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.nums):
            return -1
            
        real_val = (self.multiplier * self.nums[idx] + self.increment) % self.MOD
        return real_val
