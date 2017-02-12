# coding:utf8
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        # 解法简单
        # 首先建立score和rank的映射
        # 其次对于原始的score查找dict对应的rank，拼接为list
        # 特殊处理1 2 3 名

        # sort_nums = sorted(nums)
        #
        # # 建立映射
        # res = {num:str(i+1) for i,num in enumerate(sort_nums[::-1])}
        #
        # # 查找dict
        # # 获取结果list
        # ranks = []
        # for num in nums:
        #     ranks.append(res[num])
        #
        # # 特殊处理 1 2 3名
        # for i,rank in enumerate(ranks):
        #     if rank == '1':
        #         ranks[i] = 'Gold Medal'
        #     elif rank == '2':
        #         ranks[i] = 'Silver Medal'
        #     elif rank == '3':
        #         ranks[i] = 'Bronze Medal'
        # return ranks


        # Another solution
        # 更加python
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(nums) + 1)))

        # zip 再 dict 是建立一种一一对应的关系
        # 在这里是score和rank的映射
        # map的第一个参数是函数，指定要对第二个参数的list做什么操作
        # 在这里参数是dict的get函数
        # 对于每个nums中的score都会从dict中查找值，也就是对应的rank
        # 结果封装在map中然后再转为list

        return list(map(dict(zip(sort, rank)).get, nums))

if __name__ == '__main__':
    print(Solution().findRelativeRanks([5, 3, 4, 2, 1]))
