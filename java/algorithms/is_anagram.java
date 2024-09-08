class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();

        if (s.length() != t.length()) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
            char sChar = s.charAt(i);
            char tChar = t.charAt(i);

            sMap.put(sChar, sMap.getOrDefault(sChar, 0) + 1);
            tMap.put(tChar, tMap.getOrDefault(tChar, 0) + 1);
        }

        return sMap.equals(tMap);
    }
}