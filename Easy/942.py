class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lower, upper = 0, 0
        answer = [0]
        for i in s:
            if i == "I":
                upper += 1
                answer.append(upper)
            elif i == "D":
                lower -= 1
                answer.append(lower) 
        return [i-lower for i in answer]
