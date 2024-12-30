class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {'[' : ']', '{':'}', '(':')'}
        stk = []
        for c in s:
            if c in paren_map.keys():
                stk.append(c)
            elif c in paren_map.values():
                if stk == []: return False
                if c != paren_map.get(stk.pop()):
                    return False
        if stk != []:
            return False
        return True