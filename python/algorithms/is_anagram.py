from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tCount = Counter(t)
        sCount = Counter(s)
        if tCount == sCount:
            return True
        else:
            return False