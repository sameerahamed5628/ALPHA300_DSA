class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        check=s+s
        m=len(check)
        n=len(goal)
        for i in range(m-n+1):
            x=True
            for j in range(n):
                if check[i+j]!=goal[j]:
                    x=False
                    break
            if x:
                return True
        return False