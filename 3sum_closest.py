# coding:utf8
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # special case
        if len(nums)<3:
            return 0

        nums.sort()
        res_left, res_right = -float('inf'), float('inf')
        for i in range(len(nums)-2):
            # skip for the same value
            if i > 0 and nums[i] == nums[i-1]: i+=1

            l,r=i+1,len(nums)-1

            while l<r:
                # 区别
                # 记录s
                # 更新他
                s = nums[i]+nums[l]+nums[r]
                if s < target:
                    l+=1
                    # while l<r and nums[l] == nums[l+1] : l+=1
                    # update the left result
                    res_left = max(res_left,s)
                elif s>target:
                    r-=1
                    # while l < r and nums[r] == nums[r - 1]: r -= 1
                #     update right result
                    res_right = min(res_right,s)

                else:
                    return s
        # return result
        return res_left if (target-res_left) < (res_right - target) else res_right

if __name__ == '__main__':
    print(Solution().threeSumClosest([-1,0,1,1,55],3))