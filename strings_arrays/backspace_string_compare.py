import itertools

class Solution(object):
    def backspaceCompare(self, s, t):
        def valid_index(s, i):
            backslash = 0
            while i >= 0:
                if backslash == 0 and s[i] != '#':
                    break
                elif s[i] == '#':
                    backslash += 1
                else:
                    backslash -= 1
                i -= 1
            return i
        
        i_s, i_t = len(s) - 1, len(t) - 1
        while i_s >= 0 or i_t >= 0:
            i_s = valid_index(s, i_s) 
            i_t = valid_index(t, i_t) 

            char_s = s[i_s] if i_s >= 0 else ""
            char_t = t[i_t] if i_t >= 0 else ""

            if char_s != char_t:
                return False
            
            i_s -= 1
            i_t -= 1
        
        return True
    
    def backspaceCompare0(self, s, t):
        temp1, temp2 = "", ""

        for c in s:
            if c == '#':
                temp1 = temp1[:len(temp1)-1]
            else:
                temp1 += c
        
        for c in t:
            if c == "#":
                temp2 = temp2[:len(temp2)-1]
            else:
                temp2 += c
        
        return temp1 == temp2
    
    def backspaceCompare1(self, s, t):
        def process(string):
            result = []
            for c in string:
                if c == '#':
                    if result:
                        result.pop()
                else:
                    result.append(c)
            return result

        return process(s) == process(t)
    
    def backspaceCompare2(self, s, t):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(s), F(t)))
        