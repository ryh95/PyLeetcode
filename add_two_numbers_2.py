# coding:utf8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # step 1
        # 获取l1 l2 的值
        l1_val = self.node2num(l1)
        l2_val = self.node2num(l2)


        # step 2
        # 将2个值相加
        total_val = l1_val+l2_val

        # step 3
        # 将和重新拼接为list
        return self.num2node(total_val)


    def node2num(self, string_nodes):
        '''

        :param string_nodes: ListNode
        :return:
        '''
        num = ''
        p = string_nodes
        while p != None:
            num += str(p.val)
            p=p.next
        return int(num)

    def num2node(self,num):
        '''

        :param num: int
        :return:
        '''
        num = str(num)


        i = ListNode(int(num[0]))
        head = i
        for c in num[1:]:
            j = ListNode(int(c))
            i.next = j
            i = j
        return head

if __name__ == "__main__":
    a=ListNode(3)
    b = ListNode(2)
    a.next = b

    test = Solution().num2node(32)

    print(Solution().node2num(test))