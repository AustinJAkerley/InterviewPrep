#include <unordered_map>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) 
    {
        unordered_map<int, int> numMap;
        for(int i = 0; i < numbers.size(); i++)
        {
            int diff = target - numbers[i];
            if (numMap.find(diff) != numMap.end())
            {
                vector<int> result = {numMap[diff]+ 1, i + 1};
                return result;
            }
            numMap[numbers[i]] = i;
        }
    }
};
