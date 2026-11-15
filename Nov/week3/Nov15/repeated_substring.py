class Solution(object):
    def repeatedSubstringPattern(self, s):
        n=len(s)
        for x in range(1,n//2+1):
            if n%x==0:
                sub=s[:x]
                if sub*(n//x)==s:
                    return True
        return False
