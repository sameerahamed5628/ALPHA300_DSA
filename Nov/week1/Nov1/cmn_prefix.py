class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs)<2:
            return strs[0]
        refer=strs[0]
        for x in range(len(refer)):
            ch=refer[x]
            for word in strs[1:]:
                if x>=len(word) or word[x]!=ch:
                    return refer[:x]
            
        return refer