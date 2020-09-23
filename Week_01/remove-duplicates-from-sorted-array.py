#coding:utf-8
#2020-09-23 22:00
#本题思路如果想到双指针就比较简单，两个初始指针指向第一个和第二个元素，每次判断两个指针的元素是否相等, 若两个元素相等，向右移动右指针，然后下一次循环回来继续判断两个指针，若值不相同，则向右移动左指针，然后将右指针的元素赋值给左指针的值，最后返回left + 1即可

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
        return left + 1
