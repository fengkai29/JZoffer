# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = 0
        b = 1
        temp = 0
        while(n>1):
            temp = a+b
            a = b
            b = temp
            n = n-1
        return temp