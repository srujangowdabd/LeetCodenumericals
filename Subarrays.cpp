class Solution {
public:
    long long countConsistent(vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        long long ans = 0;

        // Stores {and_val, left_start, left_end} partitioning [0..r]
        struct AndRange {
            int val;
            int l;
            int r;
        };

        vector<AndRange> cur_ands;
        vector<int> mono; // Strictly increasing values of nums[mono[k]]

        for (int i = 0; i < n; ++i) {
            int x = nums[i];

            // Maintain monotonic stack for minimum values of subarrays ending at i
            while (!mono.empty() && nums[mono.back()] >= x) {
                mono.pop_back();
            }
            mono.push_back(i);

            // Update bitwise AND ranges ending at i
            vector<AndRange> next_ands;
            next_ands.reserve(cur_ands.size() + 1);

            for (const auto& seg : cur_ands) {
                int nval = seg.val & x;
                if (!next_ands.empty() && next_ands.back().val == nval) {
                    next_ands.back().r = seg.r;
                } else {
                    next_ands.push_back({nval, seg.l, seg.r});
                }
            }

            if (!next_ands.empty() && next_ands.back().val == x) {
                next_ands.back().r = i;
            } else {
                next_ands.push_back({x, i, i});
            }

            cur_ands.swap(next_ands);

            // Count consistent subarrays ending at i
            int m = static_cast<int>(mono.size());
            for (const auto& seg : cur_ands) {
                // Binary search for seg.val in strictly increasing nums[mono[0..m-1]]
                int lo = 0, hi = m - 1, found = -1;
                while (lo <= hi) {
                    int mid = lo + (hi - lo) / 2;
                    if (nums[mono[mid]] == seg.val) {
                        found = mid;
                        break;
                    } else if (nums[mono[mid]] < seg.val) {
                        lo = mid + 1;
                    } else {
                        hi = mid - 1;
                    }
                }

                if (found != -1) {
                    int min_l = (found == 0) ? 0 : (mono[found - 1] + 1);
                    int min_r = mono[found];

                    int ov_l = max(seg.l, min_l);
                    int ov_r = min(seg.r, min_r);
                    if (ov_l <= ov_r) {
                        ans += static_cast<long long>(ov_r - ov_l + 1);
                    }
                }
            }
        }

        return ans;
    }
};
