class Solution(object):
    def reverseWords(self, s):
        rslt = ""
        for st in s.split():
            rslt += st[::-1]
            rslt += " "
        
        return rslt.rstrip()