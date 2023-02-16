class Solution(object):
    def restoreString(self, s, indices):
        tuples = []
        for i in range(len(indices)):
            tuples.append([indices[i],s[i]])
        
        tuples.sort(key=lambda x:x[0])
        
        ret = []
        for tup in tuples:
            ret.append(tup[1])
        
        return "".join(ret)