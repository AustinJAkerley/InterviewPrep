#include <unordered_map>
#include <string>
using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_char_map;
        unordered_map<char, int> t_char_map;
        if (s.length() != t.length())
        {
            return false;
        }
        for(int i=0;i<s.length();i++)
        {
            if(s_char_map[s.at(i)])
            {
                s_char_map[s.at(i)] = s_char_map[s.at(i)] + 1;
            }
            else {s_char_map[s.at(i)] = 1;}
            if(t_char_map[t.at(i)])
            {
                t_char_map[t.at(i)] = t_char_map[t.at(i)] + 1;
            }
            else {t_char_map[t.at(i)] = 1;}
        }
        bool result = (s_char_map == t_char_map) ? true : false;
        return result;
    }
};
