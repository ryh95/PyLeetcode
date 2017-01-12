# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l=0
        q = head
        while q != None:
            l+=1
            q = q.next

        i,j = head,head
        p=0
        while j != None:
            if p == l-n:
                if p == 0:
                    head = head.next
                    return head
                i.next = j.next
                break
            i = j
            j = j.next
            p+=1
        return head

if __name__ == '__main__':
    a=ListNode(1)
    b=ListNode(2)
    c=ListNode(3)
    d=ListNode(4)
    a.next = b
    b.next = c
    c.next = d

    p = a
    while p != None:
        print(p.val)
        p = p.next


    p = Solution().removeNthFromEnd(a,4)
    while p != None:
        print(p.val)
        p = p.next
