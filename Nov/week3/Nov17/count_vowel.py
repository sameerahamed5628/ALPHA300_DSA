class Solution(object):
    def countVowelSubstrings(self, word):
        vow=['a','e','i','o','u']
        count=0
        for left in range(len(word)):
            build={}
            for right in range(left,len(word)):
                ch=word[right]
                if ch not in vow:
                    break
                if ch in build:
                    build[ch]+=1
                else:
                    build[ch]=1
                if len(build)==len(vow):
                    count+=1
        return count