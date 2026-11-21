class Solution(object):
    def buddyStrings(self, s, goal):
        if len(s)!=len(goal):
            return False
        diff=0
        place=[]
        for x in range(len(s)):
            if s[x]!=goal[x]:
                diff+=1
                place.append(x)
        if diff>2:
            return False
        new=list(s)
        check=list(goal)
        if diff==2:
            i,j=place
            new[i],new[j]=new[j],new[i]
            return new==check
        for i in range(len(new)):
            for j in range(i+1,len(new)):
                new[i],new[j]=new[j],new[i]
                if new==check:
                    return True
                new[i],new[j]=new[j],new[i]
        return False