class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = 0
        no_rob = 0
        for money in nums:
            new_rob = no_rob + money
            new_no_rob = max(rob, no_rob)
            rob = new_rob
            no_rob = new_no_rob

        return max(rob, no_rob)