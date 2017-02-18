# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None : return None
        l,i=head,head.next
        r=i.next if i != None else None
        head.next = None
        while i != None:
            i.next = l
            l = i
            i = r
            r = r.next if r != None else None
        return l

if __name__ == "__main__":
    a=ListNode(1)
    b=ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c

    s = Solution().reverseList(ListNode(1))

    print('Done')