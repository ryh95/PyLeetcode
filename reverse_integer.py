class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            ret = int(str(x)[::-1])
            if ret > 2**31 -1:
                return 0
            else:
                return ret
        else:
            x = -x
            ret = -int(str(x)[::-1])
            if ret < -2**31 :
                return 0
            else:
                return ret

if __name__ == '__main__':
    a = Solution()
    print(a.reverse(1534236469))