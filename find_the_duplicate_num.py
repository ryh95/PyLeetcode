class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        return self.binary_search(1,len(nums)-1)

    def binary_search(self,l,r):
        mid = l+int((r-l)/2)
        left = self.get_direction(mid)

        if not isinstance(left,bool): return left

        if left:
            return self.binary_search(l,mid-1)
        else:
            return self.binary_search(mid+1,r)


    def get_direction(self,n):
        less,equal,beyond = 0,0,0
        for num in self.nums:
            if num == n:
                equal += 1
            elif num < n:
                less += 1
            else:
                beyond += 1
        if equal > 1: return n

        if less <= n-1:
            return False
        else:
            return True

if __name__ == "__main__":
    # [2, 3, 5, 1, 5, 6, 4]
    # [7, 9, 7, 4, 2, 8, 7, 7, 1, 5]
    print(Solution().findDuplicate([7, 9, 7, 4, 2, 8, 7, 7, 1, 5]))