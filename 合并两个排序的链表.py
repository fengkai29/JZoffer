# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        m = n = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                m.next = pHead1
                m = m.next
                pHead1 = pHead1.next
            else:
                m.next = pHead2
                m = m.next
                pHead2 = pHead2.next

        if pHead1:
            m.next = pHead1
        else:
            m.next = pHead2
        return n.next
