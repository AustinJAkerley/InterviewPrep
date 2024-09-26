#include <unordered_set>
#include <unordered_map>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) 
    {
        unordered_set<int> numSet;
        int largest = 0;
        for(auto num: nums)
        {
           numSet.insert(num);
        }

        for(auto num: numSet)
        {
            if(numSet.count(num-1))
            {
                continue;
            }
            else
            {
                int size = 1;
                int new_num = num + 1;
                while(numSet.count(new_num))
                {
                    new_num++;
                    size++;
                }
                if(size > largest)
                {
                    largest = size;
                }
            }
        }
        return largest;
    }
};
