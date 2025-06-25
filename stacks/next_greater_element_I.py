class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        hashmap = {v:i for i, v in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                idx = hashmap[val]
                res[idx] = nums2[i]

            if nums2[i] in hashmap:
                stack.append(nums2[i])
        
        return res
    
    def nextGreaterElement0(self, nums1, nums2):
        hashmap = {v:i for i, v in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] in hashmap:
                for j in range(i+1, len(nums2)):
                    if nums2[j] > nums2[i]:
                        idx = hashmap[nums2[i]]
                        res[idx] = nums2[j]
                        break
        
        return res
        