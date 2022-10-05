class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        answer = [0, 0]
        for element in position:
            if element%2 == 0:
                answer[1] += 1
            else:
                answer[0] += 1
        return min(answer)
