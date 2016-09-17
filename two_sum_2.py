class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # pass the duplicates before binary search
        # independent
        ans = []
        for i in xrange(len(numbers)):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            if target-numbers[i] in numbers[i+1:]:
                ans.append(i)
                ans.append(numbers[i+1:].index(target-numbers[i])+(i+1))
                break
        # cause the index is not zero-based
        ans = [i+1 for i in ans]
        return ans