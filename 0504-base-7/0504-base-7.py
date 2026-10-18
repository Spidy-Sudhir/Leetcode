class Solution:
    def convertToBase7(self, n: int) -> str:
        if n == 0:
            return "0"
        is_negative = n < 0
        n = abs(n)
        res = ""
        while n > 0:
            res += str(n % 7)
            n //= 7
        return f"-{res[::-1]}" if is_negative else res[::-1]
