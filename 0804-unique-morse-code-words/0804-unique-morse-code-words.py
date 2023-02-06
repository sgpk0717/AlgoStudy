from collections import defaultdict

class Solution(object):
    trans = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    def uniqueMorseRepresentations(self, words):
        dt = defaultdict(int)
        
        for word in words:
            mos = ""
            
            for ch in word:
                mos += self.trans[ord(ch)-ord('a')]
            
            dt[mos] += 1
        
        return len(list(dt.keys()))
        
        