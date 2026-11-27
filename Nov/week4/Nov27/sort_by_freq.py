class Solution(object):
    def frequencySort(self, s):
        doop={}
        for x in s:
            if x in doop:
                doop[x]+=1
            else:
                doop[x]=1
        out=[]
        while doop:
            l=max(doop,key=doop.get)
            n=doop[l]
            for y in range(n):
                out.append(l)
            del doop[l]
        return "".join(out)