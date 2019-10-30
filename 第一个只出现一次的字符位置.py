class Solution:
    def FirstNotRepeatingChar(self, s):
        a = list(s)
        i = 0
        for i in range(len(s)):
            temp = a[0]
            del a[0]
            if temp not in a:
                return i
            a.append(temp)
        if i==len(s):
            return -1