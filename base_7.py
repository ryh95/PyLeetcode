class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = ''
        flag = False
        if num == 0: return '0'
        if num < 0:
            num = -num
            flag = True
        while num!=0:
            ret+=str(num%7)
            num = int(num/7)
        if flag :
            return '-'+ret[::-1]
        else:
            return ret[::-1]

if __name__ == "__main__":
    print(Solution().convertToBase7(0))