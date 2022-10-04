class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        if numRows == 1:
            return dp
        for i in range(1, numRows):
            tmp = [0] + dp[-1] + [0]
            dp.extend([[tmp[i] + tmp[i+1] for i in range(len(tmp)-1)]])
        return dp
