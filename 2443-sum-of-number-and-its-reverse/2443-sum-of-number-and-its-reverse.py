class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        # if num ==0:
        #     return True
        def reverse(num):
            s = str(num)
            return int(s[::-1])
        for i in range(num+1):
            if i + reverse(i) == num:
                return True
        else:
            return False