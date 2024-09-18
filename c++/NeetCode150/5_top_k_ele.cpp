#include <unordered_map>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) 
    {
        unordered_map<int, int> num_count;
        for(auto& it: nums)
        {
            if (num_count.find(it) != num_count.end())
            {
                num_count[it]+=1;
            }
            else 
            {
                num_count[it] = 1;
            }
        }
        vector<int> output;
        for(int i=0; i<k; i++)
        {
            int biggest = 0;
            int index;
            for(auto& kv: num_count)
            {
                cout << kv.first << " " << kv.second << endl;
                if (kv.second > biggest)
                {
                    index = kv.first;
                    biggest = kv.second;
                }
            }
            output.push_back(index);
            num_count.erase(index);
        }
        return output;
    }
};
