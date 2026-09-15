class Solution:
    def largestOverlap(self, g1: List[List[int]], g2: List[List[int]]) -> int:
        f = lambda g1,g2,n=len(g1):max(sum(sum(map(mul,r1[j:],r2)) 
            for r1,r2 in zip(g1[i:],g2)) for i in range(n) for j in range(n))
        return max(f(g1,g2),f(g2,g1),f(g1[::-1],g2[::-1]),f(g2[::-1],g1[::-1]))