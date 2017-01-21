class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # special case
        if n == 0:
            return True

        f = [0 for i in range(n)]
        r = [0 for i in range(n)]

        f[0],r[0] = 0,1

        for i in range(1,n):
            f[i] = max((i-1+nums[i-1])*r[i-1],f[i-1])
            r[i] = 1 if f[i] >= i else 0

        return True if r[n-1] == 1 else False

if __name__ == '__main__':
    print(Solution().canJump([0,2,3]))