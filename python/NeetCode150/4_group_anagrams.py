from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            s_list = anagrams.get(s_sorted, []) # List to be stored as the value, based off the counter as the key
            s_list.append(s)
            anagrams.update({s_sorted:s_list})
        return [anagram_list for anagram_list in anagrams.values()]