#include <unordered_map>
#include <string>
using namespace std;

class Solution 
{
public:
    int lengthOfLongestSubstring(string s) 
    {
        // Special Case
        if (s.size() < 2) return s.size();

        // Base Case
        int l = 0;
        int r = 1;
        int longest = 1;
        
        unordered_map<char, int> charMap;
        charMap[s[l]] = 1;
        while (r < s.size())
        {
            while(charMap.find(s[r]) != charMap.end()) 
            {
                charMap.erase(s[l]);
                l += 1;
            }
            charMap[s[r]] = 1;
            longest = max(longest, r - l + 1);
            r += 1;
        }
        return longest;
    }
};
