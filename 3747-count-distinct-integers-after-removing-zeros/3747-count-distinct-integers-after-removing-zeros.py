class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        m = len(s)
        pow9 = pow(9, m)
        ans = (pow9 - 9)//8 
        for digit in map(int, s):
            if digit == 0: return ans
            pow9//= 9
            ans+= (digit - 1) * pow9
        return ans + 1