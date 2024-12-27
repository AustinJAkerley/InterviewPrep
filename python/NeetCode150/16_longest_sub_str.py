class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Special cases
        if len(s) < 2: return len(s)

        # General cases
        l = 0
        r = 0
        charMap = {}
        longest = 1
        while r < len(s):
            while s[r] in charMap:
                charMap.pop(s[l])
                l += 1
            charMap[s[r]] = 1
            longest = max(longest, r -l + 1)
            r += 1
        return longest