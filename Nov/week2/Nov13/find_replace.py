class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        out=[]
        for word in words:
            s=word
            map1={}
            map2={}
            check=True
            for i in range(len(s)):
                x=s[i]
                y=pattern[i]
                if x in map1 and map1[x]!=y:
                    check=False
                    break
                if y in map2 and map2[y]!=x:
                    check=False
                    break
                map1[x]=y
                map2[y]=x
            if check==True:
               out.append(s)
        return out