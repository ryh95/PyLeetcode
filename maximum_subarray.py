class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time limit exceed
        # O(n^2) solution
        n = len(nums)
        f = [0 for y in range(n)]

        res = -float('inf')
        for i in range(n):
            for j in range(n-i):
                if j <1:
                    f[j] = nums[i]
                else:
                    f[j] = f[j-1]+nums[i+j]

                res = max(res,f[j])
        return res

    def maxSubArray2(self,nums):
        # O(n) solution
        n = len(nums)
        f = [0 for y in range(n)]
        f[0] = nums[0]

        res = f[0]

        for i in range(1,n):
            f[i] = nums[i] + (f[i-1] if f[i-1] > 0 else 0)
            res = max(res,f[i])

        return res

if __name__ == '__main__':
    print(Solution().maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))
