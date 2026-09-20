# class Solution:
#     def reverseDegree(self, s: str) -> int:
#         total = 0
#         for i in range(len(s)):
#             val = (ord(s[i]) - ord('a') + 1) * (i+1 )
#             total += val
#         return total

class Solution:
    def reverseDegree(self, s: str) -> int:
        ans, idx = 0, 1
        for ch in s:
            ans+= (123 - ord(ch)) * idx
            idx+= 1
        return ans    