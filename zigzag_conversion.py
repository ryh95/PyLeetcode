class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        init,flag = 0,True
        row_nums = []

        if numRows == 1:
            return s

        for i in range(len(s)):

            row_nums.append(init)
            if flag:
                init += 1
            else:
                init -= 1

            if init == numRows-1 or init == 0:
                flag = not flag

        ans = {}
        for num in range(numRows):
            ans[num] = ''

        for i,row_num in enumerate(row_nums):
            ans[row_num] += s[i]

        ret = ''
        for num in range(numRows):
            ret += ans[num]

        return ret



if __name__ == '__main__':
    print(Solution().convert("PAYPALISHIRING", 3))