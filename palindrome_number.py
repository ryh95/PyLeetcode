class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # negative x
        if x<0:
            return False

        i,j=0,0
        while 10 ** i <= x:
            i += 1
        i -= 1

        while j <= int(i/2):
            if int(x/(10 ** j))%10 != int(x/(10 ** (i-j)))%10:
                break
            j += 1

        if j <= int(i/2):
            return False
        else:
            return True

if __name__ == '__main__':
    print(Solution().isPalindrome(-1))