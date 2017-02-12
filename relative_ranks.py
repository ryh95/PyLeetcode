class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sort_nums = sorted(nums)

        res = {num:str(i+1) for i,num in enumerate(sort_nums[::-1])}

        ranks = []
        for num in nums:
            ranks.append(res[num])

        # special case
        for i,rank in enumerate(ranks):
            if rank == '1':
                ranks[i] = 'Gold Medal'
            elif rank == '2':
                ranks[i] = 'Silver Medal'
            elif rank == '3':
                ranks[i] = 'Bronze Medal'
        return ranks

