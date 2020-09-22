#coding:utf-8
#2020-09-22 23:35
#只存储前两个元素,其余元素均靠公式递推，故空间复杂度为O（1）


class Solution:
    def climbStairs(self, n):
        if n==1 or n==2:
            return n
        first, second, res = 1, 2, 0
        for i in xrange(3, n+1):
            res = first + second
            first = second
            second = res
        return res
