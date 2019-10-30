# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if len(ss) <= 0:
            return []
        res = list()
        self.perm(ss, res, '')
        uniq = list(set(res))
        return sorted(uniq)

    def perm(self, ss, res, path):
        if ss == '':
            res.append(path)
        else:
            for i in range(len(ss)):
                self.perm(ss[:i] + ss[i + 1:], res, path + ss[i])
