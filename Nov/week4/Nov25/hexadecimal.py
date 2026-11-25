class Solution(object):
    def toHex(self, num):
        if num==0:
            return "0"
        if num<0:
            num+=2**32
        
        h="0123456789abcdef"
        hexx=[]
        while num>0:
            hexx.append(h[num%16])
            num=num//16
        return "".join(reversed(hexx))       