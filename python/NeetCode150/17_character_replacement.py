class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Special Case
        if len(s) < 2: return len(s)
        
        # Normal Case
        l = 0
        r = 1
        char_to_count = {}
        longest = 1
        char_to_count.update({s[l]:1})
        while r < len(s):
            count = char_to_count.get(s[r], 0)
            char_to_count.update({s[r]:count+1})
            while self.moveLeft(char_to_count.values(), k):
                l_count = char_to_count.get(s[l])
                char_to_count.update({s[l]:l_count - 1})
                l += 1
            longest = max(longest, r - l + 1)
            print("r: " + str(r) + "    l: " + str(l))
            r += 1
        return longest
            
    
    def moveLeft(self, counts: int, k: int) -> bool:
        mySum = 0
        largest = -1
        print(counts)
        for count in counts:
            if count > largest: largest = count
            mySum += count
            print("Diff: "+str(mySum - largest))
            if mySum - largest > k: return True
            
        return False
        