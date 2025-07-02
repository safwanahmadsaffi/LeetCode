class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> rsum(nums.size());  // ← yeh INT nahi, vector<int> hoga
        int sum = 0;                    // ← total jamaa karne ke liye

        for (int i = 0; i < nums.size(); ++i) {
            sum += nums[i];   // purana sum + current number
            rsum[i] = sum;    // rsum ke i‑th index par total daal do
        }
        return rsum;          // nayi list wapas bhej do
    }
};
