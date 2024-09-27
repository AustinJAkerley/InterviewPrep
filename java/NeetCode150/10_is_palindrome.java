class Solution {
    public boolean isPalindrome(String s) 
    {
        String cleaned_s = "";
        for(int i=0; i<s.length(); i++)
        {
            int c = (int)s.charAt(i);
            if((int)'A' <= c && (int)'Z' >= c)
            {
                cleaned_s = cleaned_s + (char)(c + (int)'a' - (int)'A');
            }
            else if((int)'0' <= c && (int)'9' >= c)
            {
                cleaned_s = cleaned_s + (char)(c);
            }
            else if((int)'a' <= c && (int)'z' >= c)
            {
                cleaned_s = cleaned_s + (char)(c);
            }
        }
        System.out.println(cleaned_s);
        if(cleaned_s.length() < 2)
        {
            return true;
        }
        for(int i = 0; i < (cleaned_s.length() / 2) + 1; i++)
        {
            if(cleaned_s.charAt(i) != cleaned_s.charAt(cleaned_s.length() - i - 1))
            {
                return false;
            }
        }
        return true;
    }
}
