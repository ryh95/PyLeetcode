class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for index,i in enumerate(s):
            if index == 0:
                stack.append(i)
                continue
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i in list(map.keys()):
                try:
                    if stack[-1] == map[i]:
                        stack.pop()
                    else:
                        stack.append(i)
                except IndexError:
                    stack.append(i)

        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    print(Solution().isValid('['))