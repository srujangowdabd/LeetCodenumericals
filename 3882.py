class Solution(object):
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])

        mx = 1 << max(max(row) for row in grid).bit_length()

        dp = [[[False] * mx for _ in range(n)] for _ in range(2)]

        dp[0][0][grid[0][0]] = True

        for i in range(m):
            for j in range(n):
                x = grid[i][j]

                if i == 0 and j == 0:
                    continue

                for k in range(mx):
                    dp[i & 1][j][k] = False

                    if i > 0 and dp[(i - 1) & 1][j][k ^ x]:
                        dp[i & 1][j][k] = True

                    if j > 0 and dp[i & 1][j - 1][k ^ x]:
                        dp[i & 1][j][k] = True

        for k in range(mx):
            if dp[(m - 1) & 1][n - 1][k]:
                return k
