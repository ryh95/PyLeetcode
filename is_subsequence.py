#coding:utf8
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
        从后向前
        two pointer
        PS:
        还可以
        从前向后
        two pointer
        '''
        i = len(s)-1
        j = len(t)-1
        # bound
        if i == -1:
            return True
        elif j == -1 and i != -1:
            return False
        while j >= 0:
            if t[j] == s[i]:
                i -= 1
                j -= 1
            else:
                j -= 1
        if i >= 0:
            return False
        else:
            return True