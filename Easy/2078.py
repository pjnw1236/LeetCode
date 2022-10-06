class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        answer = 0
        for i in range(len(colors)):
            for j in range(i+1, len(colors)):
                if colors[i] != colors[j]:
                    answer = max(answer, j-i)
        return answer
