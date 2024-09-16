#include <unordered_map>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> target_iterator_map;
        for(int i=0; i<nums.size(); i++)
        {
            if(target_iterator_map.find(nums[i]) != target_iterator_map.end())
            {
                return {target_iterator_map[nums[i]], i};
            }
            target_iterator_map[target-nums[i]] = i;
        }
        return {0,0};
    }
};
