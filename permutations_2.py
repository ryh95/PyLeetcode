# Todo;fix bug
class Solution(object):
    def permuteUnique(self, nums):
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

        elem,ans,rets,self.mydict= None, [], [], {}

        for i,item in enumerate(nums):
            elem = nums[i]

            b=nums[:]
            b.pop(i)

            try:
                if self.mydict[tuple(b)]:
                    continue
            except KeyError:
                rets = self._f(b)
                self.mydict[tuple(b)] = rets

            for ret in rets:
                ans.append([elem]+ret)

        return ans

if __name__ == '__main__':
     print(Solution().permuteUnique([3,3,0,3]))