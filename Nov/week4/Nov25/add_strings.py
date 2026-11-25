class Solution(object):
    def addStrings(self, num1, num2):
        carry=0
        out=""
        n=max(len(num1),len(num2))
        for i in range(1,n+1):
            add=carry
            if i<=len(num1):
                add+=ord(num1[-i])-ord('0')
            if i<=len(num2):
                add+=ord(num2[-i])-ord('0')
            out=str(add%10)+out
            carry=add//10
        if carry:
            out='1'+out
        return out