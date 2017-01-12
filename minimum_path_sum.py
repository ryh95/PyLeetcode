class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n_row = len(grid)
        n_col = len(grid[0])

        f = [[0 for x in range(n_col)] for y in range(n_row)]

        for i in range(n_row):
            for j in range(n_col):
                if i == 0 and j == 0:
                    f[i][j] = grid[i][j]
                elif j<1:
                    f[i][j] = f[i-1][j] + grid[i][j]
                elif i<1:
                    f[i][j] = f[i][j-1] + grid[i][j]
                else:
                    f[i][j] = min(f[i][j-1],f[i-1][j])+grid[i][j]

        return f[n_row-1][n_col-1]

if __name__ == '__main__':
    print(Solution().minPathSum([[0]]))