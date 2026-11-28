class Solution(object):
    def longestWord(self, words):
        word=words.sort()
        build=set([""])
        longg=""
        for x in words:
            if x[:-1] in build:
                build.add(x)
                if len(x)>len(longg):
                    longg=x
        return longg