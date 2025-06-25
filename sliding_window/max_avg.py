# 643. Maximum Average Subarray I

class Solution(object):
    def findMaxAverage(self, nums, k):
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]
        
        max_avg = curr_sum / float(k)

        for i in range(k, len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]

            avg = curr_sum / float(k)
            max_avg = max(max_avg, avg)
        
        return max_avg
        