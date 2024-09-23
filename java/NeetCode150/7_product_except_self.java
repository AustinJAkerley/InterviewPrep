class Solution {
    public int[] productExceptSelf(int[] nums) 
    {
        int zero_count = 0;
        int product = 1;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i] == 0)
            {
                zero_count++;
            }
            else
            {
                product = product * nums[i];
            }
        }
        int[] output = new int[nums.length];
        for(int i=0; i<nums.length;i++)
        {
            if(zero_count==0)
            {
                output[i] = product / nums[i];
            }
            else if(zero_count==1)
            {
                if(nums[i] == 0)
                {
                    output[i] = product;
                }
                else
                {
                    output[i] = 0;
                }
            }
            else if(zero_count>=2)
            {
                output[i] = 0;
            }
        }
        return output;
    }
}  