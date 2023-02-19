class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        def backtrack(start: int, path: List[str], res: List[List[str]]) -> None:
            if start == len(s):
                res.append(path[:])
                return
            
            for i in range(start, len(s)):
                if dp[start][i]:
                    path.append(s[start:i+1])
                    backtrack(i+1, path, res)
                    path.pop()
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
        
        res = []
        backtrack(0, [], res)
        return res