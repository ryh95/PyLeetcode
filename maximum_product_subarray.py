class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TLE
        # 2d array
        f = [([0] * len(nums)) for i in range(len(nums))]
        # init
        for i in xrange(len(nums)):
            f[i][i] = nums[i]
        for window in xrange(1,len(nums)+1):
            for i in xrange(len(nums)-window):
                j = i + window
                if j-1 >= i+1:
                    # e.g f[0][3]
                    # core algorithm
                    sum = 1
                    for x in xrange(i,j+1):
                        sum *= nums[x]
                    f[i][j] = max(f[i+1][j],f[i+1][j-1],f[i][j-1],sum)
                else:
                    # e.g f[0][1]
                    f[i][j] = max(f[i+1][j],f[i][j-1],nums[i]*nums[j])
        return f[0][len(nums)-1]