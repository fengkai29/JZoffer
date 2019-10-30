class Solution:
    def PrintFromTopToBottom(self, root):
        m = []
        if root == None:
            return m
        else:
            a = []
            a.append(root)
            while len(a):
                temp = a.pop(0)
                m.append(temp.val)
                if temp.left:
                    a.append(temp.left)
                if temp.right:
                    a.append(temp.right)
            return m
