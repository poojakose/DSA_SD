class Solution(object):
    def isValid(self, s):
        pairs = {'}':'{', ')':'(', ']':'['}
        stack = []

        for c in s:
            if stack and c in pairs:
                if pairs[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        if stack:
            return False

        return True