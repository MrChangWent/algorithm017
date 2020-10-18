

class Solution:
    def myPow(self, x, n):
        if n < 0:
            return self.myPow(1/x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        return x * self.myPow(x, n - 1)



class Solution:
    def myPow(self, x, n):
        if n < 0:
            x, n = 1/x, -n
        if n == 0:
            return 1
        result = 1
        for _ in xrange(n):
            result *= x
        return result


class Solution:
    def myPow(self, x, n):
        if n < 0:
            return self.myPow(1/x, -n)
        if n == 0:
            return 1
        if n % 2 == 0:
            return self.myPow(x*x, n//2)
        else:
            return x * self.myPow(x*x, n//2)
