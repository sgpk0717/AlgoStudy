from collections import Counter

class Solution(object):
    def commonChars(self, words):
        rets = []
        cts = []
        for word in words:
            cts.append(Counter(word))
        for ch in words[0]:
            ex = True
            for ct in cts:
                if not ct[ch] > 0:
                    ex = False
            
            if ex:
                for ct in cts:
                    ct[ch] -= 1
                rets.append(ch)
                
        return rets
            
                        
                        
        