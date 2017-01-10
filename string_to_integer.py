class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        dict =  ['0','1','2','3','4','5','6','7','8','9','+','-']
        try:
            str = str.strip()

            for i,char in enumerate(str):
                if char not in dict:
                    str = str[:i]
                    break

            ans = int(str)
            if ans > 2147483647:
                return 2147483647
            elif ans < -2147483648:
                return -2147483648
            return ans

        except ValueError as e:
            return 0

if __name__ == '__main__':
    print(Solution().myAtoi("  -0012a42"))