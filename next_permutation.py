class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def swap(j, i):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        n = len(nums)
        i = n-1
        while i>=1:
            if nums[i-1]<nums[i]:
                break
            i-=1
        if i == 0:
            return nums.sort()

        num, pos= float('inf'),None
        for x in range(i,n):
            if nums[x]>nums[i-1] and min(num,nums[x])<num:
                pos = x

        swap(i-1,pos)

        nums[i:] = nums[i:][::-1]

if __name__ == '__main__':
    nums = [1,2,3,0]
    Solution().nextPermutation(nums)

    print(nums)