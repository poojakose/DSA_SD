class Solution(object):
    def maxFrequencyElements(self, nums):
        counter = {}
        freq = 0

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

            if counter[n] > freq:
                freq = counter[n]

        result = 0
        for v in counter.values():
            if v == freq:
                result += v
        
        return result
    
    def maxFrequencyElements1(self, nums):
        counter = {}
        freq = 0

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

            if counter[n] > freq:
                freq = counter[n]
                
        tmp = list(counter.values())
        count = tmp.count(freq)
               
        return freq * count
