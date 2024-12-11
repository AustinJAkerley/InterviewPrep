import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) 
    {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        for(int i=0; i<nums.length; i++)
        {
            int a = nums[i];
            if(i != 0 && nums[i] == nums[i-1])
            {
                continue;
            }
            int l = i + 1;
            int r = nums.length - 1;
            while( l < r)
            {
                int sum = a + nums[l] + nums[r];
                if(sum < 0)
                {
                    l += 1;
                }
                else if(sum > 0)
                {
                    r -= 1;
                }
                else
                {
                    result.add(Arrays.asList(a, nums[l], nums[r]));
                    l += 1;
                    while(l < r && nums[l] == nums[l-1])
                    {
                        l += 1;
                    }
                }
            }
        }
        return result;
    }
}
