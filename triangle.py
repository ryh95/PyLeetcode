class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        f = [([0]*len(triangle)) for _ in xrange(len(triangle))]
        # special
        if len(triangle) == 0 or len(triangle[0]) == 0:
            return 0
        # init
        f[0][0] = triangle[0][0]
        # core algorithm
        for i in xrange(1,len(triangle)):
            for j in xrange(i+1):
                if j > 0 and j < i:
                    f[i][j] = min(f[i-1][j-1]+triangle[i][j],f[i-1][j]+triangle[i][j])
                elif j == 0:
                    f[i][j] = f[i - 1][j] + triangle[i][j]
                elif j == i:
                    f[i][j] = f[i -1][j-1] + triangle[i][j]
        return min(f[len(triangle)-1])