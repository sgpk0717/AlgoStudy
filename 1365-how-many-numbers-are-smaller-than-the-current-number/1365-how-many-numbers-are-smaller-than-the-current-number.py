from collections import Counter

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ct = Counter(nums)
        smct = [0 for _ in range(101)]
        
        ct_keys = sorted(list(ct.keys()))
        for i in range(len(ct_keys)):
            smallers = 0
            for j in range(i):
                smallers += ct[ct_keys[j]]
            if smallers > 0:
                smct[ct_keys[i]] = smallers
        
        ret = []
        for num in nums:
            ret.append(smct[num])
        return ret
        