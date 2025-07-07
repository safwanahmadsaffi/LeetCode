class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int X = 0;
        for (const string& op : operations) {
            if (op[1] == '+')
                ++X;   // barhao
            else
                --X;   // ghatao
        }
        return X;
    }
};
