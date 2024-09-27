class Solution {
    public int[] twoSum(int[] numbers, int target) 
    {
        HashMap<Integer, Integer> numMap = new HashMap<Integer, Integer> ();
        for(int i = 0; i < numbers.length; i++)
        {
            Integer diff = target - numbers[i];
            if(numMap.containsKey(diff))
            {
                int[] result = new int[2];
                result[0] = numMap.get(diff) + 1;
                result[1] = i + 1;
                return result;
            }
            numMap.put(numbers[i], i);
        }
         return new int[0];
    }
}
