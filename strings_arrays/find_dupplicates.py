# class Solution(object):
#     def findDuplicate(self, nums):
#         nums.sort()
#         l, r = 0, 1
        
#         while r < len(nums):
#             if nums[l] == nums[r]:
#                 return nums[l]
#             l += 1
#             r += 1

#         return

class Solution(object):
    def findDuplicates(self, nums):
        res = []
        for n in nums:
            n = abs(n)
            if nums[n-1] < 0:
                res.append(n)
            nums[n-1] = -nums[n-1]
        
        return res
        