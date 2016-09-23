class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f =  [0]*(len(nums)+1)
        if len(nums) == 0:
            return 0
        f[0] = 0
        f[1] = nums[0]
        for i in xrange(2,len(nums)+1):
            f[i] = max(f[i-1],f[i-2]+nums[i-1])
        return f[-1]