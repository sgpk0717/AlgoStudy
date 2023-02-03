class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return False

        list_s = list(s)
        list_t = list(t)

        list_s.sort()
        list_t.sort()

        for i in range(len(list_s)):
            if list_s[i] != list_t[i]:
                return False
        return True
        