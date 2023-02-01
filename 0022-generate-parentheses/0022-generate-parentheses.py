class Solution(object):
    answers = []
    N = 0

    def generateParenthesis(self, n):
        self.N = n * 2
        self.answers = []
        self.generateDFS("(", 1, 1)

        return self.answers

    def generateDFS(self, pth, s, l):
        if s > self.N // 2:
            return

        if l == self.N:
            if s == 0:
                self.answers.append(pth)
            return

        self.generateDFS(pth + "(", s + 1, l + 1)

        if s > 0:
            self.generateDFS(pth + ")", s - 1, l + 1)