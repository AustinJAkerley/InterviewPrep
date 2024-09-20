class Solution {
    public int[] productExceptSelf(int[] nums) 
    {
        int[] output = new int[nums.length];
        int product = 1;
        int zero_counter = 0;
        for(int i = 0; i<nums.length;i++)
        {
            if(nums[i]==0)
            {
                zero_counter++;
            }
            else
            {
                product = product * nums[i];
            }
        }
        for(int i = 0; i<nums.length;i++)
        {
            if(zero_counter == 0)
            {
                output[i] = product/nums[i];
            }
            else if(zero_counter == 1)
            {
                if(nums[i]==0)
                {
                    output[i] = product;
                }
                else
                {
                    output[i] = 0;
                }
            }
            else
            {
                output[i] = 0;
            }
        }
        return output;
    }
}  
