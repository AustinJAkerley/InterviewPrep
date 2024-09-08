#include <set>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> numSet;
        numSet = set<int>(nums.begin(), nums.end());

        if (numSet.size() == nums.size())
        {
            return false;
        }
        else
        {
            return true;
        }
    }
};
