class Solution(object):
    def interpret(self, command):
        new=[]
        for i in range(len(command)):
            if command[i]=="G" or command[i]=="a" or command[i]=="l":
                new.append(command[i])
            elif command[i]=="(" :
                if command[i+1]==")":
                    new.append("o")
                else:
                    continue
        return "".join(new)
