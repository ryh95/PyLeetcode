# coding:utf8
class Solution(object):
    # def findDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Todo:以后再做一遍
        res = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return res

if __name__ == "__main__":
    print(Solution().findDuplicates([4,3,2,7,7,2,3,1]))