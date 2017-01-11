class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time limit exceed
        matrix = [[0 for x in range(len(nums))] for y in range(len(nums))]
        # init
        for i in range(len(nums)):
            matrix[i][i] = nums[i]

        if len(nums) == 1:
            return nums[0]

        #
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                matrix[i][j] = matrix[i][j - 1] + nums[j]

        for i, list in enumerate(matrix):
            matrix[i] = list[i:]

        ans = []
        for list in matrix:
            for i in list:
                ans.append(i)

        return max(ans)

if __name__ == '__main__':
    print(Solution().maxSubArray([1]))
