class Solution(object):
    def isPalindrome(self, s):
        pal=[]
        new=s.lower()
        for ch in new:
            if ch.isalnum():
                pal.append(ch)
        left=0
        right=len(pal)-1
        while left<right:
            if pal[left]==pal[right]:
                left+=1
                right-=1
            else:
                return False
        return True