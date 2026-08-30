class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        total = 0
        for v in nums:
            width, d = v % 10, v // 10
            dStr = str(d)
            x, y = int(dStr[:width]), int(dStr[width:])
            val = pow(x, y, MOD)
            total = (total + val) % MOD
        return total