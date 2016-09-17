class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # haven't passed test yet
        ans = self.find(0,len(s),s)
        return ans

    def hasRepeatingCharacters(self,s):
        '''

        :param s: str
        :return: bool
        '''
        if len(set(s)) == len(s):
            return False
        else:
            return True

    def find(self,start,end,s):

        ans = (start + end) / 2

        if start == ans:
            return ans

        flag = 1
        for i in range(len(s)-ans):
            sub = s[i:i+ans]
            if not self.hasRepeatingCharacters(sub):
                flag = 0
                break

        if flag == 1:
            end = ans
        else:
            start = ans

        return self.find(start, end, s)

