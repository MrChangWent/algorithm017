#coding:utf-8
#2020-09-22 23:40
#基本思路还是比较简单的，left和right分别指向起点和终点，同时开始遍历，每次移动较小的那个指针，left就向右，right就向左，同时res始终保存所有结果中的最大值，直到不满足left<right，则返回结果


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
		res, left, right = 0, 0, len(height) - 1
		while left < right:
			area = min(height[left], height[right]) * (right - left)
			res = max(res, area)
			if height[left] < height[right]:
				left += 1
			else:
				right -= 1
		return res

