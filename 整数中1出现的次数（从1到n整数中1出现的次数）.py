# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for temp in range(1,n+1):
            num = temp
            while num>0:
                if num%10 == 1:
                    count = count + 1
                num = int(num /10)
        return count
