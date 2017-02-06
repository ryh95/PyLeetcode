class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s=''.join([c for c in s if c.isalpha() or c.isdigit()])

        if len(s) == 0 : return True
        l,u=0,len(s)-1
        while l<=u:
            if s[l]!=s[u]:
                return False
            l+=1
            u-=1
        return True

if __name__ == '__main__':
    print(Solution().isPalindrome('A man, a plan, a canal: Panama'))