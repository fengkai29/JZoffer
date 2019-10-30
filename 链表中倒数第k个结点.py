# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        m = head
        count = 0
        while head != None:
            head = head.next
            count = count + 1
        if k > count:
            return None
        for i in range(1,count-k+1):
            m = m.next
        return m