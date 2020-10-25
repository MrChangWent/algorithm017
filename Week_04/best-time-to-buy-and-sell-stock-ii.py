class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        def dfs(index,status):
            if index==n:
                return 0
            a = dfs(index+1,status)
            b,c = 0,0
            if status:
                b = dfs(index+1,0)+prices[index]
            else:
                c = dfs(index+1,1)-prices[index]
            return max(a,b,c)
        return dfs(0,0)

class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        d = dict()
        def dfs(index,status):
            if (index,status) in d:
                return d[index,status]
            if index==n:
                return 0
            a,b,c = 0,0,0
            a = dfs(index+1,status)
            if status:
                b = dfs(index+1,0)+prices[index]
            else:
                c = dfs(index+1,1)-prices[index]
            d[index,status] = max(a,b,c)
            return d[index,status]
        return dfs(0,0)

class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        dp0 = 0
        dp1 = -prices[0]
        for i in xrange(1,n):
            tmp = dp0
            dp0 = max(dp0,dp1+prices[i])
            dp1 = max(dp1,tmp-prices[i])
        return max(dp0,0)
