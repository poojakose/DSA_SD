## 424. Longest Repeating Character Replacement

class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        l, res = 0, 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res
        
    def characterReplacement0(self, s, k):
        count = {}
        l, res = 0, 0
        maxF = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])

            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res
        