# coding:utf8
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 解法1
        # 固定前面两个数，排序情况下寻找第三个数
        # O(N^2logN)

        # nums.sort()
        # solutionList = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if -(nums[i]+nums[j]) in nums[j+1:]:
        #             solution = []
        #             solution.append(nums[i]), solution.append(nums[j]), solution.append(-(nums[i]+nums[j]))
        #             solutionList.append(solution)
        # # remove duplicate list in list of lists
        # # reference: http://stackoverflow.com/questions/2213923/python-removing-duplicates-from-a-list-of-lists
        # for i in solutionList:
        #     i.sort()
        # solutionList.sort()
        # solutionList = list(a for a,_ in itertools.groupby(solutionList))
        # return solutionList
        #

        # 解法2
        # 排序
        # 固定第一个数
        # 寻找后面2个数使得和是负的第一个数
        # 问题退化为2sum
        # O(N^2)
        # Strange : it is slower than the first version

        nums.sort()
        solutionList = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                # skip the duplicate
                continue
            l,u = i+1,len(nums)-1
            while l<u:
                s = nums[i]+nums[l]+nums[u]
                # 0 is the target
                if s < 0:
                    l+=1
                elif s>0:
                    u-=1
                else:
                    # solution = []
                    # solution.append(nums[i]),solution.append(nums[l]),solution.append(nums[u])
                    solutionList.append((nums[i],nums[l],nums[u]))
                    while l<u and nums[l] == nums[l+1]:
                        # skip the duplicate
                        l+=1
                    while l<u and nums[u] == nums[u-1]:
                        # skip the duplicate
                        u-=1
                    # solutionList.append(solution)
        #             IMPORTANT
        #             otherwise there will be infinite loop
                    l+=1;u-=1
        return solutionList

if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))