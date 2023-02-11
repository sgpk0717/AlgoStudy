from collections import defaultdict

class Solution(object):
    def countPoints(self, rings):
        dts = [defaultdict(int) for _ in range(10)]
        rings = list(rings)
        for i in range(0,len(rings),2):
            
            dts[int(rings[i+1])][str(rings[i])] += 1
        
        rets = 0
        for dt in dts:
            if len(list(dt.keys())) == 3:
                rets += 1
            
        return rets