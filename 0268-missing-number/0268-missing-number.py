from collections import Counter

class Solution(object):
    def missingNumber(self, nums):
        N = len(nums)
        s = (N+1)*N // 2
        return s - sum(nums)
        