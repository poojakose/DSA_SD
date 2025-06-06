class Solution(object):
    def findDisappearedNumbers(self, nums):
        available = set(nums)
        result = []

        for n in range(1, len(nums)+1):
            if n not in available:
                result.append(n)

        return result
        