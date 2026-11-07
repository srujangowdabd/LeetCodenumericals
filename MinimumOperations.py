
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {

        vector<bool> seen(k + 1, false);
        int count = 0;

        for (int i = nums.size() - 1; i >= 0; i--) {

            if (nums[i] <= k && !seen[nums[i]]) {
                seen[nums[i]] = true;
                count++;
            }

            if (count == k) {
                return nums.size() - i;
            }
        }

        return nums.size();
    }
};
