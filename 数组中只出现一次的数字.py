class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        a = []
        count = 0
        for i in range(len(array)):
            temp = array[0]
            del array[0]
            if temp not in array:
                a.append(temp)
            array.append(temp)
        return a