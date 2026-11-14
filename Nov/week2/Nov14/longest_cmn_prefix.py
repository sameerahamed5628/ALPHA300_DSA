class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs)<2:
            return strs[0]
        refer=strs[0]
        for i in range(len(refer)):
            x=refer[i]
            for word in strs[1:]:
                if i>=len(word) or word[i]!=x:
                    return refer[:i]
        return refer 
