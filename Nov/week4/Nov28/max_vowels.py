class Solution(object):
    def maxVowels(self, s, k):
        vow="aeiou"
        maax=0
        count=0
        for i in range(k):
            if s[i] in vow:
                count+=1
        maax=count
        for j in range(k,len(s)):
            if s[j] in vow:
                count+=1
            if s[j-k] in vow:
                count-=1
            maax=max(maax,count)
        return maax