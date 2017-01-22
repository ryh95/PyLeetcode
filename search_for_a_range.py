# coding:utf8
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Todo:整理题解！
        ans = []
        if len(nums) == 0: return [-1,-1]
        l = self._findLowerBound(nums, target, 0, len(nums) - 1)
        u = self._findUpperBound(nums, target, 0, len(nums) - 1)

        if l == len(nums):
            ans.append(-1)
        else:
            if nums[l] == target:
                ans.append(l)
            else:
                ans.append(-1)

        ans.append(u-1 if nums[u-1] == target else -1)

        return ans

    def _findUpperBound(self,nums,target,l,u):
        #找到第一个大于target的数的位置（下标从0开始）
        # http://stackoverflow.com/questions/12144802/finding-multiple-entries-with-binary-search
        if l > u:
            return l

        mid = l + ((u - l) >> 1)

        if nums[mid] > target:
            return self._findUpperBound(nums, target, l, mid - 1)
        else:
            return self._findUpperBound(nums, target, mid + 1, u)

    def _findLowerBound(self,nums,target,l,u):
        # 找到第一个大于等于target的数的位置（下标从0开始）
        # http://stackoverflow.com/questions/12144802/finding-multiple-entries-with-binary-search
        if l > u:
            return l

        mid = l + ((u-l) >> 1)

        if nums[mid] >= target:
            return self._findLowerBound(nums,target,l,mid-1)
        else:
            return self._findLowerBound(nums,target,mid+1,u)


if __name__ == '__main__':
    print(Solution().searchRange([1,2,2,3],2))