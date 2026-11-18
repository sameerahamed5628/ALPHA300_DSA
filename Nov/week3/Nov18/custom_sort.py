class Solution(object):
    def customSortString(self, order, s):
        build={}
        for x in s:
            if x in build:
                build[x]+=1
            else:
                build[x]=1

        word=list(order)
        string=list(s)
        kept=[]
        for y in word:
            if y in string:
                kept.append(y)
        word=kept
                
        out=[]
        for z in word:
            out.append(z*build[z])
            del build[z]
        for i in build:
            out.append(i*build[i])
        return "".join(out)
