class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[1 for i in range(n+1)]
        dp[1]=1
        dp[2]=1
        for i in range(3,n+1):
            maxi=-1
            for j in range(i-1,i//2-1,-1):
                vals=[maxi,j*(i-j),dp[j]*(i-j),j*dp[i-j],dp[j]*dp[i-j]]
                maxi=max(vals)
            dp[i]=maxi
        return dp[n]