#include <unordered_map>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) 
    {
        string cleaned_s = "";
        for(int i = 0; i < s.size(); i++)
        {
            if(static_cast<int>('A') <= static_cast<int>(s[i]) && static_cast<int>('Z') >= static_cast<int>(s[i]))
            {
                int lower_c = static_cast<int>(s[i]) - static_cast<int>('A') + static_cast<int>('a');
                cleaned_s = cleaned_s + static_cast<char>(lower_c);
            }
            else if(static_cast<int>('a') <= static_cast<int>(s[i]) && static_cast<int>('z') >= static_cast<int>(s[i]))
            {
                cleaned_s = cleaned_s + s[i];
            }
            else if(static_cast<int>('0') <= static_cast<int>(s[i]) && static_cast<int>('9') >= static_cast<int>(s[i]))
            {
                cleaned_s = cleaned_s + s[i];
            }
        }
        // cout << cleaned_s << " " << ((cleaned_s.size() / 2) + 1) << endl;;

        if(cleaned_s.size() < 2) {return true;}

        for(int i = 0; i < ((cleaned_s.size() / 2) + 1); i++)
        {
            // cout << cleaned_s[i] << " " << cleaned_s[cleaned_s.size() - 1 - i] << endl;
            if(cleaned_s[i] != cleaned_s[cleaned_s.size() - 1 - i]) {return false;}
        }
        return true;
    }
};
