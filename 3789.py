class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        return (
            min(cost1, costBoth) * need1 +
            min(cost2, costBoth) * need2
            if costBoth >= cost1 + cost2
            else min(
                costBoth * max(need1, need2),
                costBoth * min(need1, need2)
                + cost1 * (need1 - min(need1, need2))
                + cost2 * (need2 - min(need1, need2))
            )
        )
