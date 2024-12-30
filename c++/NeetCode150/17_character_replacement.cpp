#include <string>
#include <unordered_map>


using namespace std;
class Solution 
{
public:
    int characterReplacement(string s, int k) 
    {
        // Special Case
        if (s.size() < 2) return s.size();

        // Standard Case
        int l = 0;
        int r = 1;
        int longest = 1;
        unordered_map<char, int> char_to_count;
        char_to_count[s[l]] = 1;
        while (r < s.size())
        {
            char_to_count[s[r]] += 1;
            while(moveLeft(char_to_count, k))
            {
                char_to_count[s[l]] -= 1; 
                l += 1;
            }
            longest = max(longest, r - l + 1);
            r += 1;
        }
        return longest;
    }

    bool moveLeft(unordered_map<char, int> char_to_cnt, int k)
    {
        int sum = 0;
        int largest = 0;
        int c;
        for (const auto& count : char_to_cnt)
        {
            c = count.second;
            largest = max(largest, c);
            sum += c;
        }
        return (sum - largest > k);
    }
};
