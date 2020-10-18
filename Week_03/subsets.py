class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)
        
        def backtrack(i, tmp):
            res.append(tmp[:])
            for j in range(i, n):
                tmp.append(nums[j])
                backtrack(j + 1,tmp)
                tmp.pop()
        backtrack(0, [])
        return res  
