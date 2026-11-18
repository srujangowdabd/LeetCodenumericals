
class Solution {
public:
    int rob(vector<int>& nums) {

        int prev2 = 0;
        int prev1 = 0;

        for (int i = 0; i < nums.size(); i++) {

            int take = nums[i] + prev2;
            int notTake = prev1;

            int curr = max(take, notTake);

            prev2 = prev1;
            prev1 = curr;
        }

        return prev1;
    }
};
