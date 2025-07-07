class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int netgain = 0;
        int maxele = 0;
        for (int i=0; i< gain.size(); i++)
    {
            netgain = netgain+gain[i];
            gain[i] =  netgain ;
            if(maxele<netgain){
            maxele=netgain;
        };
    };
        return maxele;

    }
}; 