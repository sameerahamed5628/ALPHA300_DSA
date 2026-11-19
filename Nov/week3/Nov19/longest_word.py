class Solution(object):
    def findLongestWord(self, s, dictionary):
        dictionary.sort(key=lambda w:(-len(w),w))
        for word in dictionary:
            x=0
            for j in range(len(s)):
                if x<len(word) and s[j]==word[x]:
                    x+=1
                if x==len(word):
                    return word
        return ""