import java.util.HashMap;

class Solution 
{
    public int lengthOfLongestSubstring(String s) 
    {
        // Special Case
        if (s.length() < 2) return s.length();
        
        // Standard Case
        int l = 0;
        int r = 1 ;
        int longest = 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        map.put(s.charAt(l), 1);
        while (r < s.length())  
        {
            while (map.containsKey(s.charAt(r)))
            {
                map.remove(s.charAt(l));
                l+=1;
            }
            map.put(s.charAt(r), 1);
            longest = Math.max(longest, r - l + 1);
            r += 1;
        }
        return longest;
    }   
}
