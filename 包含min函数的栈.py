# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.m = []
    def push(self, node):
        # write code here
        self.m.append(node)
    def pop(self):
        # write code here
        del self.m[len(self.m)-1]
    def top(self):
        # write code here
        return self.m[0]
    def min(self):
        # write code here
        return min(self.m)