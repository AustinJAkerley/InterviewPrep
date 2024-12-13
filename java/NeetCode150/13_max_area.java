class Solution 
{
    public int maxArea(int[] heights) 
    {
        int l = 0;
        int r = heights.length - 1;
        int max_area = 0;
        while(l < r)
        {
            int area = Math.min(heights[l], heights[r]) * (r - l);
            max_area = Math.max(max_area, area);
            if(heights[l] < heights[r])
            {
                l += 1;
            }
            else
            {
                r -= 1;
            }
        }
        return max_area;
    }
}
