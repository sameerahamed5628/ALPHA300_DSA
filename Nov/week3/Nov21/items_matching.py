class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        out=0
        rule={"type":0,"color":1,"name":2}
        x=rule[ruleKey]
        for item in items:
            if item[x]==ruleValue:
                out+=1
        return out
    