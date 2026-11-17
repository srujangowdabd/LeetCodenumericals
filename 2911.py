class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        INF = float('inf')

        # Step 1: Precompute costs
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for length in range(2, n - i + 1):
                j = i + length - 1
                best = INF

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    groups = length // d

                    for r in range(d):
                        left = 0
                        right = groups - 1

                        while left < right:
                            a = s[i + r + left * d]
                            b = s[i + r + right * d]

                            if a != b:
                                changes += 1

                            left += 1
                            right -= 1

                    best = min(best, changes)

                cost[i][j] = best

        # Step 2: Dynamic Programming
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):
                for start in range(2 * (parts - 1), end - 1):
                    dp[parts][end] = min(
                        dp[parts][end],
                        dp[parts - 1][start] + cost[start][end - 1]
                    )

        return dp[k][n]
