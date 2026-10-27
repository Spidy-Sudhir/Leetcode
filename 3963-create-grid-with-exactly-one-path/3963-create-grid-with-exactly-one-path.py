class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        a = []
        for x in range(m):
            s = ""
            for y in range(n):
                if x == 0 or y == n - 1:
                    s += "."
                else:
                    s += "#"
            a.append(s)
        return a