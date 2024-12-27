import java.util.*;

class Solution 
{
    public int characterReplacement(String s, int k) 
    {
        // Special Case
        if (s.length() < 2) return s.length();
        
        // Standard Case
        int l = 0;
        int r = 1;
        int longest = 1;
        HashMap<Character, Integer> char_to_count = new HashMap<Character, Integer>();
        char_to_count.put(s.charAt(l), 1); // Initial char and count
        while (r < s.length())
        {
            char_to_count.put(s.charAt(r), char_to_count.getOrDefault(s.charAt(r), 0) + 1);
            while (moveLeft(char_to_count.values().toArray(new Integer[0]), k)) 
            {
                char_to_count.put(s.charAt(l), char_to_count.get(s.charAt(l)) - 1);
                l += 1;
            }
            longest = Math.max(longest, r - l + 1);
            r += 1;
        }
        return longest;


    }

    public boolean moveLeft(Integer[] vals, int k)
    {
        int largest = 0;
        int sum = 0;
        for(int i = 0; i < vals.length; i++)
        {
            if(vals[i] > largest) largest = vals[i] ;
            sum += vals[i];
            if(sum - largest > k) return true;
        }
        return false;
    }
}
