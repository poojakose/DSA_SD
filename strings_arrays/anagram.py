class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        hs, ht = {}, {}
        
        for i in range(len(s)):
            hs[s[i]] = 1 + hs.get(s[i], 0)
            ht[t[i]] = 1 + ht.get(t[i], 0)

        for c in hs:
            if hs[c] != ht.get(c, 0):
                return False

        return True
    
    def isAnagram2(self, s, t):
        if len(s) != len(t):
            return False

        hs, ht = {}, {}
        
        for i in range(len(s)):
            hs[s[i]] = 1 + hs.get(s[i], 0)
            ht[t[i]] = 1 + ht.get(t[i], 0)

        
        return hs == ht
    
    def isAnagram1(self, s, t):
        if len(s) != len(t):
            return False

        hs, ht = {}, {}
        
        for i in range(len(s)):
            if s[i] in hs:
                hs[s[i]] += 1
            else:
                hs[s[i]] = 1

            if t[i] in ht:
                ht[t[i]] += 1
            else:
                ht[t[i]] = 1
        
        return hs == ht
    
