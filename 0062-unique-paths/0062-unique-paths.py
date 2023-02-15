class Solution(object):
    def uniquePaths(self, m, n):
        maps = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                maps[i][j] = maps[i-1][j] + maps[i][j-1]
        
        return maps[m-1][n-1]