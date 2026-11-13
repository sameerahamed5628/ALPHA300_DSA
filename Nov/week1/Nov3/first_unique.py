class Solution(object):
    def firstUniqChar(self, s):
        entry={}
        for x in s:
            if x in entry:
                entry[x]+=1
            else:
                entry[x]=1
        for y in range(len(s)):
            if entry[s[y]]==1:
                return y
        return -1