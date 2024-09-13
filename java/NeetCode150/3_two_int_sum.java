
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> target_index_map;
        for(int i=0;i<nums.length();i++)
        {
            index = target_index_map.getOrDefault(nums[i], -1);
            if(index!=-1)
            {
                return [index, i];
            }
            target_index_map.put(target-nums[i], i);
        }
        return null;
    }
}
