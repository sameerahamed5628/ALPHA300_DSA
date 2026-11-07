class Solution(object):
    def toLowerCase(self, s):
        loww=[]
        for x in range(len(s)):
            if 65<=ord(s[x]) and ord(s[x])<=90:
                n=ord(s[x])+32
                loww.append(chr(n))
            else:
                loww.append(s[x])
        return "".join(loww)