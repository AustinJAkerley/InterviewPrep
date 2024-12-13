#include <vector>
#include <algorithm>
using namespace std;
class Solution 
{
public:
    int maxArea(vector<int>& heights) 
    {
        int l = 0;
        int r = heights.size() - 1;
        int max_area = 0;
        while(l < r)
        {
            int area = min(heights[l], heights[r]) * (r - l);
            max_area = max(max_area, area);
            if (heights[l] < heights[r])
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
};
