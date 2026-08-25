class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i = 1
        while i < max(nums)*2:
            x = i*k
            if x not in nums:
                return x
            else:
                i = i+1
