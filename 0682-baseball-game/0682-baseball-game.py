class Solution:
    def calPoints(self, operations: List[str]) -> int:
        answer = []
        for oper in operations:
            if oper == "C":
                answer.pop() 
            elif oper == "D":
                answer.append(answer[-1] * 2)
            elif oper == "+":
                answer.append(answer[-2] + answer[-1])
            else:
                answer.append(int(oper)) 
        return sum(answer)
        