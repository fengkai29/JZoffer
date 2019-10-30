class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        count = 0
        m = []
        while pHead != None:
            m.append(pHead)
            pHead = pHead.next
            if pHead in m:
                count = 1
                break
        if count:
            return pHead
        else:
            print('null')
