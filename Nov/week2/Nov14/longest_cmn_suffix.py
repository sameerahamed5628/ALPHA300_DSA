class Solution(object):
    def longestCommonsuffix(self, strs):
        rev=[]
        for word in strs:
            rev.append(word[::-1])
        refer=rev[0]
        for i in range(len(refer)):
            x=refer[i]
            for word in rev[1:]:
                if i>=len(word) or word[i]!=x:
                    return refer[:i][::-1]
        return refer[::-1]
