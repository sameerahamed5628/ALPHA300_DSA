class Solution(object):
    def uniqueOccurrences(self, arr):
        unique={}
        val=[]
        for x in arr:
            if x in unique:
                unique[x]+=1
            else:
                unique[x]=1
        for y in unique:
            val.append(unique[y])

        for  x in range(len(val)):
            for y in range(len(val)):
                if x!=y and val[x]==val[y]:
                    return False
        return True