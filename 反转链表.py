# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        a = []
        while pHead != None:
            a.append(pHead.val)
            pHead = pHead.next
        a.reverse()
        m = n = ListNode(a[0])
        for i in range(1, len(a)):
            m.next = ListNode(a[i])
            m = m.next
        return n
