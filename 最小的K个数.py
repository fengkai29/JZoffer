class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        a = []
        if k > len(tinput):
            return a
        else:
            tinput.sort()
            for i in range(k):
                a.append(tinput[i])
            return a


