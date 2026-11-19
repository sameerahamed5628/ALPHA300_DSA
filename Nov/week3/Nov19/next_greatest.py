class Solution(object):
    def nextGreatestLetter(self, letters, target):
        if letters[-1]<target:
            return letters[0]
        targett=ord(target)
        lex=[]
        for x in letters:
            lex.append(ord(x))
        
        left=0
        right=len(lex)-1
        while left!=right:
            mid=(left+right)//2
            if lex[mid]==targett:
                left=mid+1
            elif lex[mid]>targett:
                right=mid
            else:
                left=mid+1
        if lex[left]==targett:
            return letters[0]
        return chr(lex[left])