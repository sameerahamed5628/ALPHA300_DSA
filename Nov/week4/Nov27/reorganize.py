class Solution(object):
    def reorganizeString(self, s):
        doop={}
        for x in s:
            doop[x]=doop.get(x,0)+1
        n=max(doop.values())
        
        if n>(len(s)+1)//2:
            return ""
        
        build={}
        while doop:
            maax=max(doop,key=doop.get)
            build[maax]=doop[maax]
            del doop[maax]
        
        out=[]
        while build:
            have=None
            for x in build:
                if out and x==out[-1]:
                    continue
                if have==None or build[x]>build[have]:
                    have=x
            out.append(have)
            build[have]-=1
            if build[have]==0:
                del build[have]
        return "".join(out)
                
                