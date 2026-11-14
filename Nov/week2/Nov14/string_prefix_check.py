class Solution(object):
    def isPrefixString(self, s, words):
        x=0
        for word in words:
            y=len(word)+x
            if word==s[x:y]:
                x=y
                if x==len(s):
                    return True
            else:
                return False
        return False