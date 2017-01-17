class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i,j,res=0,1,-float('inf')

        if n==0:
            return 0
        elif n == 1:
            return 1

        map={}
        map[s[i]] = 1
        l = 1
        while j<n:
            try:
                while map[s[j]] == 1:
                    del map[s[i]]
                    l-=1
                    i+=1
            except KeyError:
                map[s[j]] = 1
                j+=1
                l+=1
            res = max(res,l)
        return res

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('dvdf'))