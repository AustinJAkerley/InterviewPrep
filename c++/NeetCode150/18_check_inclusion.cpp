#include <string>
#include <unordered_map>

using namespace std;
class Solution 
{
public:
    bool checkInclusion(string s1, string s2) 
    {
        if (s2.size() < s1.size())
        {
            return false;
        }

        unordered_map<char, int> s1_char_to_count;
        unordered_map<char, int> s2_char_to_count;

        for(int i = 0; i < s1.size(); i++)
        {
            s1_char_to_count[s1[i]] += 1;
            s2_char_to_count[s2[i]] += 1;
        }

        for(int i = 0; i < s2.size() - s1.size(); i++)
        {
             if (s1_char_to_count == s2_char_to_count) return true;

            // Remove the character going out of the window
            char leftChar = s2[i];
            s2_char_to_count[leftChar]--;
            if (s2_char_to_count[leftChar] == 0)
            {
                s2_char_to_count.erase(leftChar);
            }

            // Add the character coming into the window
            char rightChar = s2[i + s1.size()];
            s2_char_to_count[rightChar]++;
        }
        return (s1_char_to_count == s2_char_to_count);
    }
};
