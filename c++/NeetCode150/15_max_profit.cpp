using namespace std;
class Solution 
{
public:
    int maxProfit(vector<int>& prices) 
    {
    int l = 0;
    int r;
    int max_prof = 0;
    while(l+1 < prices.size() && prices[l+1] < prices[l]) l+=1;

    r = l + 1;
    while(r < prices.size())
    {
        max_prof = max(max_prof, prices[r]-prices[l]);
        if (prices[r] < prices[l]) l = r;
        r+=1;

    }

    return max_prof;    
    }
};
