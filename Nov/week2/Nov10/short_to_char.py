class Solution(object):
    def shortestToChar(self, s, c):
        new=[]
        i=0
        x=0
        last=-len(s)
        while i<len(s):
            if s[i]!=c:
                i+=1
            else:
                for y in range(x,i):
                    n=min(i-y,y-last)
                    new.append(n)
                new.append(0)
                x=i+1
                last=i
                i+=1
        for z in range(x,len(s)):
            n=z-last
            new.append(n)
        return new