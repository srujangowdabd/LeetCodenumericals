 * @param {number[]} nums
 * @return {number}
 */
var maxSelectedElements = function(nums) {
    nums.sort((a, b) => a - b);

    const dp = new Map();
    let ans = 0;

    for (const x of nums) {
        const nextLen = (dp.get(x) || 0) + 1;
        dp.set(x + 1, nextLen);
        if (nextLen > ans) ans = nextLen;

        const curLen = (dp.get(x - 1) || 0) + 1;
        dp.set(x, curLen);
        if (curLen > ans) ans = curLen;
    }

    return ans;
};
