class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagram_groups = new HashMap<String, List<String>>();
        for(int i = 0; i<strs.length; i++)
        {
            char[] c = strs[i].toCharArray();
            Arrays.sort(c);
            String sorted_s = new String(c);
            List<String> new_list;
            List<String> anagram_list = anagram_groups.getOrDefault(sorted_s, new ArrayList<>());
            anagram_list.add(strs[i]);
            anagram_groups.put(sorted_s, anagram_list);
        }
        return new ArrayList<>(anagram_groups.values());
    }
}
