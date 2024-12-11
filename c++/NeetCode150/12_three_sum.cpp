#include <vector>
#include <algorithm>
using namespace std;
class Solution 
{
    public:
    vector<vector<int>> threeSum(vector<int>& nums) 
    {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        for(int i = 0; i<nums.size(); i++)
        {
            if (i > 0 && nums[i] == nums[i-1])
            {
                continue; // Skipping duplicates
            }
            int a = nums[i];
            int l = i + 1;
            int r = nums.size() - 1;
            while(l < r)
            {
                int sum = a + nums[l] + nums[r];
                if(sum >  0)
                {
                    r -= 1;
                }
                else if(sum < 0)
                {
                    l += 1;
                }
                else
                {

                    result.push_back({a, nums[l], nums[r]});
                    l += 1;
                    while(l < r && nums[l-1] == nums[l])
                    {
                        l +=1;
                    }
                }
            }
        }
        return result;
    }
};
