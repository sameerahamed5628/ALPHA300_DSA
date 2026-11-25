class Solution(object):
    def addBinary(self, a, b):
        n=max(len(a),len(b))
        binary=""
        carry=0
        for i in range(1,n+1):
            x=carry
            if i<=len(a) and a[-i]=='1':
                x+=1
            if i<=len(b) and b[-i]=='1':
                x+=1
            
            if x>1:
                carry=1
                if x==2:
                    binary="0"+binary
                else:
                    binary="1"+binary
            else:
                carry=0
                binary=str(x)+binary
        if carry:
            binary="1"+binary
        return binary
