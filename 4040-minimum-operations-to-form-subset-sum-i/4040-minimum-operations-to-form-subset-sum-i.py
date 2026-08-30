class Solution:
    def minOperations(self, nums, target):
        dp = [float('inf')] * (target + 1)
        dp[0] = 0
        for x in nums:
            opts = []
            v, k = x, 0
            while v <= target:
                opts.append((v, k))
                v *= 2; k += 1
            v, d = x, 1
            while v > 0:
                v //= 2
                if v > 0 and v <= target: opts.append((v, d))
                d += 1
            ndp = dp[:]
            for val, cost in opts:
                for s in range(target, val - 1, -1):
                    if dp[s - val] < float('inf'):
                        ndp[s] = min(ndp[s], dp[s - val] + cost)
            dp = ndp
        return -1 if dp[target] == float('inf') else dp[target]