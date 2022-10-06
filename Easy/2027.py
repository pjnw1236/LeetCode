class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        answer = 0
        pointer = 0
        while True:
            if pointer >= n:
                return answer 
            if s[pointer] == "X":
                pointer += 3
                answer += 1
            else:
                pointer += 1
