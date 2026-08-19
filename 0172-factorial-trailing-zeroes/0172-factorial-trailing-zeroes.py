# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         def fac(n):
#             if n == 1 or n == 0:
#                 return 1
#             ans = n * fac(n-1)
#             return ans
#         res = fac(n)
#         count = 0
#         while res >= 1:
#             if res % 10 == 0:
#                 count +=1
#             elif res % 10 !=0:
#                 break
#             res = res//10
#         return count
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res