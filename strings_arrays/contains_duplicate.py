class Solution(object):
    def containsDuplicate(self, nums):
        tmp = set()
        for n in nums:
            if n in tmp:
                return True
            
            tmp.add(n)
        
        return False