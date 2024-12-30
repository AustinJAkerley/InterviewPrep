import java.util.HashMap;

import java.util.HashMap;

class Solution {
    public boolean checkInclusion(String s1, String s2) {
        // Special Case
        if (s1.length() > s2.length()) {
            return false;
        }

        // Frequency maps for s1 and the sliding window of s2
        HashMap<Character, Integer> charToCountS1 = new HashMap<>();
        HashMap<Character, Integer> charToCountS2 = new HashMap<>();

        // Initialize the frequency maps
        for (int i = 0; i < s1.length(); i++) {
            char c1 = s1.charAt(i);
            char c2 = s2.charAt(i);
            charToCountS1.put(c1, charToCountS1.getOrDefault(c1, 0) + 1);
            charToCountS2.put(c2, charToCountS2.getOrDefault(c2, 0) + 1);
        }

        // Sliding window
        for (int i = s1.length(); i < s2.length(); i++) {
            // Check if the maps are equal
            if (charToCountS1.equals(charToCountS2)) {
                return true;
            }

            // Slide the window: remove the leftmost character
            char leftChar = s2.charAt(i - s1.length());
            charToCountS2.put(leftChar, charToCountS2.get(leftChar) - 1);
            if (charToCountS2.get(leftChar) == 0) {
                charToCountS2.remove(leftChar); // Clean up to match map equality
            }

            // Add the new character
            char rightChar = s2.charAt(i);
            charToCountS2.put(rightChar, charToCountS2.getOrDefault(rightChar, 0) + 1);
        }

        // Check the final window
        return charToCountS1.equals(charToCountS2);
    }
}