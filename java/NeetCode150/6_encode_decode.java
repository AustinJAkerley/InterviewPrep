
class Solution {

    // Encodes a list of strings into a single string
    public String encode(List<String> strs) {
        StringBuilder strBuilder = new StringBuilder();
        
        if (strs.size() == 0) {
            return "";
        }
        
        if (strs.size() == 1 && strs.get(0).equals("")) {
            return "\n";
        }
        
        for (String s : strs) {
            strBuilder.append(s).append("\n");
        }
        
        return strBuilder.toString();
    }

    // Decodes a single string into a list of strings
    public List<String> decode(String str) {
        List<String> strs = new ArrayList<>();
        
        if (str.equals("")) {
            return strs;
        }
        
        if (str.equals("\n")) {
            strs.add("");
            return strs;
        }
        
        StringBuilder subStrBuilder = new StringBuilder();
        
        for (char c : str.toCharArray()) {
            if (c == '\n') {
                strs.add(subStrBuilder.toString());
                subStrBuilder.setLength(0);  // reset the string builder
            } else {
                subStrBuilder.append(c);
            }
        }
        
        return strs;
    }
}
