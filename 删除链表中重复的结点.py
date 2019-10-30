# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        b = p = ListNode(0)
        if pHead is None or pHead.next is None:
            return pHead
        count = pHead.val
        if pHead.val != pHead.next.val:
            b.next = ListNode(pHead.val)
            b = b.next
            count = pHead.val
            pHead = pHead.next
        while pHead.next != None:
            if pHead.val != count and pHead.val != pHead.next.val:
                b.next = ListNode(pHead.val)
                b = b.next
            count = pHead.val
            pHead = pHead.next
        if pHead.val != count:
            b.next = ListNode(pHead.val)
        return p.next