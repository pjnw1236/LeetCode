class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        answer = 0
        for i in range(len(number)):
            if number[i] == digit:
                tmp = int(number[:i] + number[i+1:])
                answer = max(answer, tmp) 
        return str(answer)
        
