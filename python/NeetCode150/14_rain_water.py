class Solution:
    def trap(self, heights: List[int]) -> int:
        l = 0
        end = len(heights) - 1
        total_water = 0
        if len(heights) < 2:
            return 0

        # Remove any leading or trailing 0s
        while (heights[l] == 0):
             l+=1
        while (heights[end] == 0):
             end-=1

        # Remove any stairs that water could not hold.
        while (heights[l+1] >= heights[l]):
             l+=1
        while (heights[end-1] >= heights[end]):
            end-=1
        
        # To the right of l and the the left of r there will have to be water.
        r = l + 1
        while (r < end):
            while heights[l] > heights[r] and r < end: #
                r += 1
            while max(heights[l+1],  heights[r]) > heights[r]:
                l += 1
            min_height = min(heights[l], heights[r]) # Water lvl
            for wata in range(l+1, r):
                total_water += min_height - heights[wata]
            l = r
            r+=1
        return total_water
            
             
            


