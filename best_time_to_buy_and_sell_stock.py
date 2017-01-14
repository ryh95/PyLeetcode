class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # O(n) solution
        # f and t can remove with two variables
        n = len(prices)

        if n == 0:
            return 0

        f = [0 for x in range(n)]
        t = [0 for x in range(n)]

        f[0],t[0] = 0,0

        for i in range(1,n):
            if i == 1:
                t[i] = prices[0]
            else:
                t[i] = min(t[i-1],prices[i-1])

            f[i] = max(0,prices[i]-t[i])

        return max(f)

if __name__ == '__main__':
    print(Solution().maxProfit([]))