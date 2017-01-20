class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        f = [[0 for x in range(n)] for y in range(n)]
        res = None

        # window=1
        for i in range(n):
            f[i][i] = 1
            res = s[i:i+1]

        # window=2
        for i in range(n-1):
            if s[i]==s[i+1]:
                f[i][i+1] = 1
                res = s[i:i+2]

        for w in range(3,n+1):
            for i in range(n-w+1):
                if s[i] == s[i+w-1] and f[i+1][i+w-2] == 1:
                    f[i][i+w-1] = 1
                    res = s[i:i+w]

        return res if res != None else ''

if __name__ == '__main__':
    print(Solution().longestPalindrome('abacdfgdcaba'))