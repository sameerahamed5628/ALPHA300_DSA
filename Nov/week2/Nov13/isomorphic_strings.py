class Solution(object):
    def isIsomorphic(self, s, t):
        maps={}
        mapt={}
        for i in range(len(s)):
            x=s[i]
            y=t[i]

            if x in maps and maps[x]!=y:
                return False
            if y in mapt and mapt[y]!=x:
                return False
            maps[x]=y
            mapt[y]=x
        return True