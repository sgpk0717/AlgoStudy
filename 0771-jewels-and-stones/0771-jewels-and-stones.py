from collections import Counter

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        counter = Counter(stones)
        
        ret = 0
        for ch in jewels:
            ret += counter[ch]
        return ret