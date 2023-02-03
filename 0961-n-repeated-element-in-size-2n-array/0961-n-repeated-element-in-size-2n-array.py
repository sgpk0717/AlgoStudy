from collections import Counter

class Solution(object):
    def repeatedNTimes(self, nums):
        n = len(nums) // 2
        
        cnt = Counter(nums)
        
        cnt_key = list(cnt.keys())
        cnt_val = list(cnt.values())
        
        idx = 0
        
        for i in range(len(cnt_val)):
            if cnt_val[i] == n:
                idx = i
                break
        return cnt_key[idx]
                
        