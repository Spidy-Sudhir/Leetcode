class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dic = {}
        for i in range(n):
            rem = target - nums[i]
            if rem in dic:
                return (dic[rem], i)
            dic[nums[i]] = i