class Solution(object):
    def minOperations(self, s):
        change=0
        for x in range(len(s)):
            if x%2==0:
                check='0'
            else:
                check='1'
            if s[x]!=check:
                change+=1
        return min(change,len(s)-change)