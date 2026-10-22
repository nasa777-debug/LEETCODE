class Solution:
    def interpret(self, command: str) -> str:
        r=''
        for i in range(len(command)):
            if command[i]=='G':
                r+=command[i]
            elif command[i]=='(':
                if command[i+1]==')':
                    r+='o'
                elif command[i+1]=='a' and command[i+2]=='l':
                    r+='al'
        return r