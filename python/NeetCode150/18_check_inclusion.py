from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
    
        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        for i in range(len(s1), len(s2)):
            if window_count == s1_count:
                return True
            # Add the new character to the window
            window_count[s2[i]] += 1
            # Remove the character that is sliding out of the window
            window_count[s2[i - len(s1)]] -= 1
        
        # Check the last window
        return window_count == s1_count