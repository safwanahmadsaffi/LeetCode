class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        unordered_map<int, int> freq;
        int count = 0;
        
        for (int num : nums) {
            count += freq[num];  // Each time we see num again, it can pair with all previous ones
            freq[num]++;
        }
        
        return count;
    }
};
