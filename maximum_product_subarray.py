class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        f = [0 for y in range(n)]
        t = [0 for y in range(n)]

        f[0] = nums[0]
        t[0] = nums[0]

        for i in range(1,n):
            if nums[i] > 0:
                f[i] = max(nums[i]*f[i-1],nums[i])
                t[i] = min(nums[i]*t[i-1],nums[i])
            elif nums[i]< 0:
                f[i] = max(nums[i]*t[i-1],nums[i])
                t[i] = min(nums[i]*f[i-1],nums[i])

        return max(f)

if __name__ == '__main__':
    print(Solution().maxProduct([-1]))