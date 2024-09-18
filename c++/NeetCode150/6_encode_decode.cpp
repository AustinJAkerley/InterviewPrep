#include <unordered_map>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:

    string encode(vector<string>& strs) 
    {
        string s = "";
        if(strs.size() == 0) {return "";}
        else if((strs.size() == 1) && (strs[0] == "")) {return "\n";}
        else
        {
            for(int i=0;i<strs.size();i++)
            {
                s = s + strs[i] + '\n';
            }
            return s;
        }
    }

    vector<string> decode(string s) 
    {
        vector<string> strs = {};
        if(s==""){return strs;}
        else if(s=="\n")
        {
            strs.push_back("");
            return strs;    
        }
        else
        {
            string sub_s = "";
            for(int i=0;i<s.size();i++)
            {
                if(s[i] == '\n')
                {
                    strs.push_back(sub_s);
                    sub_s = "";
                }
                else
                {
                    sub_s = sub_s + s[i];
                }
            }
            return strs;
        }
    }
};
