class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res='1'
        for i in range(n-1):
            res = self.next_count(res)
        return res


    def next_count(self,n):
        '''

        :param n: str
        :return:
        '''
        s, res, i = n, '', 0
        len_s = len(s)
        while i < len_s:
            nums = 1
            j = i + 1
            while j < len_s:
                if s[j] != s[i]:
                    break
                else:
                    nums += 1
                    j += 1
            res += str(nums) + s[i]
            i = j
        return res


if __name__ == '__main__':
    print(Solution().countAndSay(5))