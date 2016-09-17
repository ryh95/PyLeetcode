# coding:utf8
# Definition for singly-linked list.
# You should annotate the ListNode class for running code on Leetcode
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        '''
        2016.9.17
        No.203
        这是使用空的头节点的方法1
        核心思想：简单的单链表操作
        注意的点：原题目的head是第一个节点，不是空的头节点
        如果使用空的头节点方法需要自己做一个头节点出来
        '''
        # check if head is ListNode
        if not isinstance(head,ListNode):
           return head
        # init
        fakeHead = ListNode(None)
        fakeHead.next = head
        prev,pointer = fakeHead,fakeHead.next

        # begin iterating
        while pointer != None:
            if pointer.val != val:
                prev = pointer
                pointer = pointer.next
            else:
                prev.next = pointer.next
                del pointer
                pointer = prev.next

        return fakeHead.next