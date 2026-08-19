class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = m = nums[0]
        for i in range(1, len(nums)):
            a = max(nums[i], a+nums[i])
            m = max(m,a)
        return m
# class Solution:
#     def maxSubArray(self, nums: list[int]) -> int:
#         curr = best = nums[0]
#         for num in nums:
#             curr = max(num, curr + num)
#             best = max(best, curr)
#         return best