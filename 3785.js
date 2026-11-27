var maximumSaleItems = function(items, budget) {
    const n = items.length;
    const free = new Array(n).fill(0);

    // Calculate free copies for each item type
    for (let i = 0; i < n; i++) {
        const factor = items[i][0];

        for (let j = 0; j < n; j++) {
            if (i !== j && items[j][0] % factor === 0) {
                free[i]++;
            }
        }
    }

    // DP: maximum items for each exact spending amount
    const NEG = -Infinity;
    let dp = new Array(budget + 1).fill(NEG);
    dp[0] = 0;

    for (let i = 0; i < n; i++) {
        const price = items[i][1];
        const bonus = free[i];

        const next = dp.slice();

        // Process each remainder separately
        for (let r = 0; r < price && r <= budget; r++) {
            let best = NEG;

            for (let t = 1; r + t * price <= budget; t++) {
                const prev = r + (t - 1) * price;

                if (dp[prev] !== NEG) {
                    best = Math.max(best, dp[prev] - (t - 1));
                }

                const current = r + t * price;

                if (best !== NEG) {
                    next[current] = Math.max(
                        next[current],
                        best + t + bonus
                    );
                }
            }
        }

        dp = next;
    }

    return Math.max(...dp);
};
