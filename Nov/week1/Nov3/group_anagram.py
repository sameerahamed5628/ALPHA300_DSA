class Solution(object):
    def groupAnagrams(self, strs):
        code=[]
        for word in strs:
            wordsort="".join(sorted(word))
            if wordsort not in code:
                code.append(wordsort)
        n=len(code)
        out=[[] for _ in range(n)]
        for word in strs:
            wordsort="".join(sorted(word))
            for x in range(n):
                if wordsort==code[x]:
                    out[x].append(word)
        return out
                    
