class Solution(object):
    def lengthOfLastWord(self, s):
        new=[]
        i=len(s)-1
        while s[i]== " ":
            i-=1
        while i>=0 and s[i]!=" ":
            new.append(s[i])
            i-=1
        count=0
        for x in new:
            count+=1
        return count   
        