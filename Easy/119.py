class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [1] 
        if rowIndex == 0:
            return answer 
        for i in range(rowIndex):
            tmp = [0] + answer + [0]
            answer = [tmp[i] + tmp[i+1] for i in range(len(tmp)-1)]
        return answer
