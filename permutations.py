class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self._f(nums)

    def _f(self,nums):
        '''

        :param nums: list[int]
        :return: List[List[int]]
        '''
        if len(nums) == 1:
            return [nums]

        elem,ans= None,[]

        for i,item in enumerate(nums):
            elem = nums[i]

            b=nums[:]
            b.pop(i)

            rets = self._f(b)

            for ret in rets:
                ans.append([elem]+ret)

        return ans

if __name__ == '__main__':
     print(Solution().permute([1,2,3]))