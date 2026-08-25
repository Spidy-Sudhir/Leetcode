class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def solve(i):
            if i >= len(cost):
                return 0
            if i in dp:
                return dp[i]
            one_step = cost[i] + solve(i + 1)
            two_step = cost[i] + solve(i + 2)
            dp[i] = min(one_step, two_step)
            return dp[i]
        return min(solve(0), solve(1))
        # def solve(i):
        #     if i>=len(cost):
        #         return 0
        #     one_step = cost[i] + solve(i+1)
        #     two_step = cost[i] + solve(i+2)
        #     return min(one_step, two_step)
        # return min(solve(0), solve(1))
        # s = 0
        # for i in range(len(cost)):
        #     climb = cost[i] + s
        #     notclimb = s
        #     s = min(climb, notclimb)
