class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [[0 for x in range(n)] for y in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    f[i][j] = 1
                elif j<1:
                    f[i][j] = f[i-1][j]
                elif i<1:
                    f[i][j] = f[i][j-1]
                else:
                    f[i][j] = f[i-1][j] + f[i][j-1]

        return f[m-1][n-1]

if __name__ == '__main__':
    print(Solution().uniquePaths(1,2))