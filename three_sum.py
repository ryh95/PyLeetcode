# coding:utf8
import itertools
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        solutionList = []
        for i in xrange(len(nums)):
            for j in xrange(i+1,len(nums)):
                if -(nums[i]+nums[j]) in nums[j+1:]:
                    solution = []
                    solution.append(nums[i]), solution.append(nums[j]), solution.append(-(nums[i]+nums[j]))
                    solutionList.append(solution)
        # remove duplicate list in list of lists
        # reference: http://stackoverflow.com/questions/2213923/python-removing-duplicates-from-a-list-of-lists
        for i in solutionList:
            i.sort()
        solutionList.sort()
        solutionList = list(a for a,_ in itertools.groupby(solutionList))
        return solutionList