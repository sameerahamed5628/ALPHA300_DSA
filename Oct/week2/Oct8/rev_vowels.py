class Solution(object):
    def reverseVowels(self, s):
        vow=["a","e","i","o","u","A","E","I","O","U"]
        new=[]
        for x in s:
            new.append(x)
        left=0
        right=len(new)-1
        while left<right:
            if new[left] in vow:
                if new[right] in vow:
                    new[left],new[right]=new[right],new[left]
                    left+=1
                    right-=1
                else:
                    right-=1
            else:
                left+=1
        return "".join(new)
                

