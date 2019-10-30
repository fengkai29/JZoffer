# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n >= 0:
            while n>0:
                if n%2 == 1:
                    count = count +1
                n = int(n/2)
            return count
        else :
            n = n + 2147483648
            while n>0:
                if n%2 == 1:
                    count = count +1
                n = int(n/2)
            return count + 1