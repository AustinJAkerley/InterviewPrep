class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<int, int> num_count = new HashMap<int, int> ();
        for(int i=0; i<nums.length; i++)
        {
            int value = num_count.getOrDefault(nums[i], 0);
            num_count.put(nums[i], value + 1);
        }

        int[] output = new int[k];
        for(int i=0;i<k;i++)
        {
            int largest = 0;
            int num = 0;
            for (Map.Entry<int, int> mapElement : num_count.entrySet())
            {
                if(mapElement.getValue() > largest)
                {
                    largest = mapElement.getValue();
                    num = mapElement.getKey();
                }
            }
            output[i] = num;
            num_count.remove(num);
        }
        return output;
    }
}
