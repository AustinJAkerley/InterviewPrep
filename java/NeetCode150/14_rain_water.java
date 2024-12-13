class Solution 
{
    public int trap(int[] height) 
    {
        if(height.length < 3) return 0; // Can't catch water without atleast 3 elements in the array
        int l = 0;
        int end = height.length - 1;
        
        // Get rid of the uneeded height
        while(height[l] == 0) {l += 1;}
        while(height[end] == 0) {end -= 1;}

        while(l > 0 && height[l+1] > height[l]) {l+=1;}
        while(height[end-1] > height[end]) {end-=1;}

        // Removed the height not needed, start true logic.
        int r = l + 1;
        int total_water = 0;
        while (r < end)
        {
            while(height[l] > height[r] && r < end){r+=1;}
            while (Math.max(height[l+1],  height[r]) > height[r]) {l+=1;}
            int min_height = Math.min(height[l], height[r]);
            for(int i = l+1; i<r;i++)
            {
                total_water += min_height - height[i];
            }
            l = r;
            r += 1;
        }
        return total_water;
    }
}


// l = 1
// r = 2
// end = 7