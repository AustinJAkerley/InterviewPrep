class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product = 1;
        int zero_count = 0;
        for(int i = 0; i<nums.size();i++)
        {
            if(nums[i] == 0)
            {
                zero_count++;
            }
            else
            {
                product = product *nums[i];
            }
        }
        vector<int> output;
        for(int i = 0; i<nums.size();i++)
        {
            if(zero_count==0)
            {
                output.push_back(product/nums[i]);
            }
            else if(zero_count==1)
            {
                if(nums[i]==0)
                {
                    output.push_back(product);
                }
                else
                {
                    output.push_back(0);
                }
            }
            else
            {
                output.push_back(0);
            }
        }
        return output;
    }
};