class Solution:
    def interpret(self, command: str) -> str:
        answer=''
        for i in range(len(command)):
            if  i != len(command)-1 and command[i]=='(' and command[i+1] ==')':
               answer = answer + 'o'
               i=i+1
            elif command[i]=='(' or command[i] ==')':
                continue 
            else:
                answer += command[i]
        return answer 