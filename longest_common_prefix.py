class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        res = strs[0]

        for i in range(1,len(strs)):
            res = self.common_prefix(str1=res,str2=strs[i])
        return res

    def common_prefix(self,str1,str2):
        str2_len = len(str2)

        for i,char in enumerate(str1):
            if i < str2_len:
                if str1[i]!=str2[i]:
                    return str1[:i]
            else:
                return str2
        return str1

if __name__ == '__main__':
    print(Solution().longestCommonPrefix(['aab','aa','aacd']))