#coding:utf-8
#2020-10-11 22:17
#按照这节课的思路，用hash就可以大大提高查询速度，所以将之前做法的数组转换成字典，访问速度就会大大提高
#此方法是结合视频和题解而来，本身没有想到这种方法


class Solution:
    def twoSum(self,nums,target):
        d = {}
        n = len(nums)
        for x in range(n):
            if target - nums[x] in d:
                return d[target-nums[x]],x
            else:
                d[nums[x]] = x

