class Solution(object):
    def wordPattern(self, pattern, s):
        word=s.split()
        if len(pattern)!=len(word):
            return False
        map1={}
        map2={}
        for i in range(len(word)):
            x=pattern[i]
            y=word[i]
            if x in map1 and map1[x]!=y:
                return False
            if y in map2 and map2[y]!=x:
                return False
            map1[x]=y
            map2[y]=x
        return True
        