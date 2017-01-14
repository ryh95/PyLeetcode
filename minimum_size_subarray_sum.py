# algorithm is correct
# java version can ac
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # f = [[0 for x in range(y,n)] for y in range(n)]
        f = [0 for y in range(n)]

        res, flag = float('inf'), False

        for i in range(n):
            for j in range(n-i):
                if j<1:
                    f[j] = nums[i]
                else:
                    f[j] = f[j-1] +nums[i+j]

                if f[j] >= s:
                    res = min(res,j+1)
                    flag = True
                    break

        if flag:
            return res
        else:
            return 0

if __name__ == '__main__':
    print(Solution().minSubArrayLen(6,[2,3,1,2,4,3]))
