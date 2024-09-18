class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        elif len(strs) == 1 and strs[0] == "":
            return "\t"
        else:
            return "\t".join(strs)
        

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        elif s == "\t":
            return [""]
        else:
            return s.split("\t")
