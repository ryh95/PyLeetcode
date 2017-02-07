# coding:utf8
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.nums = nums
        self.cache = {}
        # special case
        if len(nums) == 0:
            return 1 if S == 0 else 0

        return self._f(0,S)

    def _f(self,i,num):
        if (i,num) not in self.cache:
            if i == len(self.nums) - 1:
            # for 0
                if num==self.nums[i] and num == 0 :
                    self.cache[(i,num)] = 2
                    return self.cache[(i,num)]

                self.cache[(i,num)] = 1 if num==self.nums[i] or num==-self.nums[i] else 0
                return self.cache[(i,num)]

            self.cache[(i,num)] = self._f(i+1,num+self.nums[i])+self._f(i+1,num-self.nums[i])
            return self.cache[(i,num)]
        return self.cache[(i,num)]

if __name__ == '__main__':
    print(Solution().findTargetSumWays([29,6,7,36,30,28,35,48,20,44,40,2,31,25,6,41,33,4,35,38],35))