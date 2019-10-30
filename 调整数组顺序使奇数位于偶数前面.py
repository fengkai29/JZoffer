# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        i = 0
        m = 0
        while m < len(array):
            if array[i] % 2 == 0:
                array.append(array[i])
                del array[i]
            else:
                i = i + 1
            m = m + 1
        return array
