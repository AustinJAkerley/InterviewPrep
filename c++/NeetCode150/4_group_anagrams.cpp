#include <algorithm>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) 
    {
        unordered_map<string, vector<string>> anagram_groups;
        for (int i = 0; i < strs.size(); i++) {
            string sorted_s = strs[i];
            sort(sorted_s.begin(), sorted_s.end());
            anagram_groups[sorted_s].push_back(strs[i]);
        }

        vector<vector<string>> grouped_anagrams;
        for (auto& kv : anagram_groups) {
            grouped_anagrams.push_back(kv.second);
        }
        
        return grouped_anagrams;
    }
};
