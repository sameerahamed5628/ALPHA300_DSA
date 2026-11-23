class Solution(object):
    def areAlmostEqual(self, s1, s2):
        left=0
        new=list(s2)
        while left<=len(new)-1:
            for right in range(left,len(new)):
                new[left],new[right]=new[right],new[left]
                if "".join(new)==s1:
                    return True
                new[left],new[right]=new[right],new[left]
            left+=1
        return False