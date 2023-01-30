from collections import Counter

class Solution(object):
    def missingNumber(self, nums):
        N = len(nums)
        s = 0
        for i in range(1,N+1):
            s += i
        return s - sum(nums)
        