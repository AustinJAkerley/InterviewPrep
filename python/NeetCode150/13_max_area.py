class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while(l < r):
            mx = max(heights[l], heights[r])
            mn = min(heights[l], heights[r])
            area = mn * (r - l)
            if area > max_area:
                max_area = area
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return max_area
        