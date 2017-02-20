# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p_m = head
        l = p_m
        i = l.next

        r = i.next if i != None else None
        c = 1
        while c < m:
            if c!= 1: p_m = p_m.next
            l = l.next if l != None else None
            i = i.next if i != None else None
            r = r.next if r != None else None
            c += 1

        p_n = l
        if n == m: return head

        while i!= None:
            i.next = l
            l = i
            i = r
            r = r.next if r != None else None
            c += 1
            if c >= n:
                break
        p_m.next = l
        p_n.next = i
        return head if m != 1 else l

if __name__ == "__main__":
    a=ListNode(3)
    b=ListNode(5)
    c=ListNode(3)
    d=ListNode(4)
    a.next = b
    # b.next = c
    # c.next = d
    sol = Solution().reverseBetween(a,1,1)
    print('Done')