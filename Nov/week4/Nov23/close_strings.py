class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1)!=len(word2):
            return False
        doop1={}
        doop2={}
        for x in word1:
            if x in doop1:
                doop1[x]+=1
            else:
                doop1[x]=1
        for y in word2:
            if y in doop2:
                doop2[y]+=1
            else:
                doop2[y]=1
        for z in doop1:
            if z not in doop2:
                return False
        for k in doop2:
            if k not in doop1:
                return False
        return sorted(doop1.values())==sorted(doop2.values())
        