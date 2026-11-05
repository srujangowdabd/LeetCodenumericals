class Solution(object):
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        n = len(grid[0])
        dp = [0] * (n + 1)
        dp[1] = 1

        for row in grid:
            right = 0

            for j in range(n):
                if row[j] == 1:
                    right, dp[j + 1] = dp[j + 1], right
                else:
                    right = (right + dp[j + 1]) % MOD
                    dp[j + 1] = right

        return right
