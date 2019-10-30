# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        b = []
        for i in range(len(A)):
            ans = 1
            for j in range(len(A)):
                if i != j:
                    ans = ans * A[j]
            b.append(ans)
        return b