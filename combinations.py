class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.a = [i+1 for i in range(n)]

        return self._f(0,k,n)

    def _f(self, p, k, n):
        if n - p < k:
            return None
        if k == 0:
            return [[]]

        elem, ans = None, []

        for i in range(p, n):
            elem = self.a[i]

            rets = self._f(i + 1, k - 1,n)

            if rets != None:
                for ret in rets:
                    ans.append([elem] + ret)

        return ans

if __name__ == '__main__':
     print(Solution().combine(4,2))