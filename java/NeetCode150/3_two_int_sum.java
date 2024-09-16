class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> target_index_map = new HashMap<Integer, Integer>();
        for(int i=0; i<nums.length; i++)
        {
            int index = target_index_map.getOrDefault(nums[i], -1);
            if(index!=-1)
            {
                int[] result = {index, i};
                return result;
            }
            target_index_map.put(target-nums[i], i);
        }
        return null;
    }
}