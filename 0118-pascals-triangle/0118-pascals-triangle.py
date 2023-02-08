class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        rslt = [[1],[1,1]]
        
        for i in range(2, numRows):
            row = []
            for j in range(0, i+1):
                if j == 0 or j == i:
                    row.append(1)
                    continue
                
                row.append(rslt[i-1][j-1] + rslt[i-1][j])
                
            rslt.append(row)
            
        return rslt
        