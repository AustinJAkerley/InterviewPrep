from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Special Case
        if len(t) > len(s): return ""

        # Standard Case
        l = 0
        r = len(t)
        t_counter = Counter(t)
        s_window = s[:len(t)]
        s_counter_window = Counter(s_window)
        sub_string = ""
        while r < len(s):
            s_counter_window[s[r]] += 1
            s_window = s[l:r+1]
            # Compare to see if the counter window contains the needed elements and their quantities 
            while self.counterContains(t_counter, s_counter_window):
                if sub_string == "" or len(s_window) < len(sub_string):
                    sub_string = s_window
                    print(sub_string)
                # Shift left pointer and remove the removed element from the s window and the counter
                s_counter_window[s[l]] -= 1
                l += 1
                s_window = s[l:r+1]

            # Move right
            r += 1
            
            
        # Last comparison
        if self.counterContains(t_counter, s_counter_window):
            if sub_string == "" or len(s_window) < len(sub_string):
                    sub_string = s_window

        return sub_string
    
    def counterContains(self, t_counter, s_counter_window) -> bool:
        for key in t_counter:
            if s_counter_window.get(key, 0) < t_counter.get(key):
                return False
        return True