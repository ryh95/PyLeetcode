class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        self.nums = nums
        res = []
        for num in findNums:
            res.append(self.get_next_greater_num(num))

        return res
    def get_next_greater_num(self,num):
        idx = self.nums.index(num)

        while idx<len(self.nums)-1:
            if self.nums[idx+1] > num:
                return self.nums[idx+1]
            idx += 1
        return -1

if __name__ == "__main__":
    print(Solution().nextGreaterElement([1],[1]))