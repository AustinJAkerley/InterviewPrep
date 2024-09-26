class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2: # String is not big enough to not be a palindrome
            return True
        # Clean the string
        cleaned_s = ""
        for c in s:
            if ord('A') <= ord(c) and ord(c) <= ord('Z'):
                cleaned_s+=c
            elif ord('a') <= ord(c) and ord(c) <= ord('z'):
                cleaned_s+=c
            elif ord('0') <= ord(c) and ord(c) <= ord('9'):
                cleaned_s+=c
        cleaned_s = cleaned_s.lower()
        print(cleaned_s)
        
        if len(cleaned_s) < 2: # String is not big enough to not be a palindrome
            return True

        # We now have a cleaned string
        print((len(cleaned_s) // 2) + 1)
        for i in range(0, (len(cleaned_s) // 2) + 1):
            if cleaned_s[i] != cleaned_s[-i - 1]:
                return False
        return True