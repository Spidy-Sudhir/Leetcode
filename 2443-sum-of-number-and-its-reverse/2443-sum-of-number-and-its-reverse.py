class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def reverse(num):
            s = str(num)
            return int(s[::-1])
        for i in range(num+1):
            if i + reverse(i) == num:
                return True
        else:
            return False