class Solution(object):
    def vowelStrings(self, words, queries):
        vow=['a','e','i','o','u']
        doop=[]
        count=0
        for word in words:
                if word[0] in vow and word[-1] in vow:
                    count+=1
                doop.append(count)
        out=[]
        for x in queries:
            start=x[0]
            end=x[1]
            if start==0:
                out.append(doop[end])
            else:
                out.append(doop[end]-doop[start-1])
        return out