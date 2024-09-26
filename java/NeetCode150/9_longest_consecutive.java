class Solution {
    public int longestConsecutive(int[] nums) 
    {
        // Create Set from array
        HashSet<Integer> numSet = new HashSet<Integer>();
        int largest = 0;
        for(int i=0;i<nums.length;i++)
        {
            numSet.add(nums[i]);
        }
        
        // Loop over array
        for(int i=0;i<nums.length;i++)
        {
            if(numSet.contains(nums[i] - 1))
            {
                continue;
            }
            else
            {
                int size = 1;
                int newNum = nums[i];
                while(numSet.contains(newNum + 1))
                {
                    size++;
                    newNum++;
                }
                if(size > largest)
                {
                    largest = size;
                }
            } 
        }
        return largest;
    }
}
