### 3. Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count = {}
        res, l = 0, 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while max(count.values()) > 1:
                count[s[l]] -= 1
                l += 1

                if not count[s[l]]:
                    count.pop(s[l])
            
            res = max(res, r-l+1)

        return res

    def lengthOfLongestSubstring0(self, s):
        count = set()
        res, l = 0, 0

        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[l])
                l += 1
                
            count.add(s[r])
            res = max(res, r-l+1)

        return res