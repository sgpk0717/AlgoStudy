class Solution(object):
    def fizzBuzz(self, n):
        rslt = []
        
        for i in range(1, n+1):
            if i % 15 == 0:
                rslt.append("FizzBuzz")
            elif i % 3 == 0:
                rslt.append("Fizz")
            elif i % 5 == 0:
                rslt.append("Buzz")
            else:
                rslt.append(str(i))
        
        return rslt