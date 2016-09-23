# # coding:utf8
# import heapq
#
#
# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         f = [0]*(amount+1)
#         f[0] = 0
#         for i in xrange(1,amount+1):
#             tmp = []
#             for j in xrange(len(coins)):
#                 if i - coins[j] >= 0:
#                     tmp.append(f[i-coins[j]])
#             if len(tmp) == 0 or max(tmp) == -1:
#                 f[i] = -1
#                 continue
#             if -1 in tmp:
#                 # find second smallest number
#                 # remove duplicate in a list
#                 listTmp = list(set(tmp))
#                 listTmp.sort()
#                 f[i] = listTmp[1] + 1
#             else:
#                 f[i] = min(tmp) + 1
#         return f[amount]
#
#
#     # # 递归version
#     # def f(self,coins,amount):
#     #     # 递归边界
#     #     if amount == 0 :
#     #         return 0
#     #     ans = [self.f(coins, amount - coin) for coin in coins if amount - coin >= 0]
#     #     # 如果没有找到解
#     #     if len(ans) == 0 or max(ans) == -1:
#     #         return -1
#     #     return min(ans)+1

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        python 有效率问题
        """

        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]