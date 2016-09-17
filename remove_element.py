# coding:utf8
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        '''
        2016.9.16
        No.27
        来日重做
        此为方法一，使用了pointer
        题目难点：不能分配额外空间
        核心思想：使用两个指针，如果当前的start是val，将start和最后的end交换，end-1，如果不是，start+1。
        最后end左面都是没有val的，end右面都是val
        将原始的nums数组以end为界划分开，选择左面即可
        '''
        start,end = 0,len(nums)-1
        while start <= end:
            if nums[start] == val:
                # swap start end
                nums[start],nums[end],end = nums[end],nums[start],end - 1
            else:
                start += 1
        nums = nums[:end+1]
        return len(nums)