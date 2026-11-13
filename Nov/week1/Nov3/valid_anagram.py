class Solution(object):
    def isAnagram(self, s, t):
        m=len(s)
        n=len(t)
        if m==n:
            if sorted(s)==sorted(t):
                return True
            else:
                return False
        else:
            return False