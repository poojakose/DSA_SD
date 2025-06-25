# 387. First Unique Character in a String
import collections

class Solution(object):
    def firstUniqChar(self, s):
        tracker = collections.defaultdict(int)
        
        for c in s:
            tracker[c] += 1
        
        for i, c in enumerate(s):
            if tracker[c] == 1:
                return i

        return -1 
        