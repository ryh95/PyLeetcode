# AC
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        return f(num,16)

def f(n,x):
    result = ''
    #
    dict = {
        10:'a',
        11:'b',
        12:'c',
        13:'d',
        14:'e',
        15:'f'
    }

    if n == 0:
        return '0'
    elif n<0:
        n = 2**32 + n


    while n != 0:
        # result += str(n%x)
        if n%x >= 10:
            result += dict[n%x]
        else:
            result += str(n % x)
        n = int(n/x)

    return result[::-1]

if __name__ == '__main__':
    print(Solution().toHex(-1))