from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        scnt = Counter(list(s))
        
        ret_str = ""
        for cnt in scnt.most_common():
            ret_str += cnt[0] * cnt[1]
        
        return ret_str