class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = 0
        for i in s:
            while True:
                if pointer >= len(t):
                    return False 
                if i == t[pointer]:
                    pointer += 1
                    break 
                pointer += 1
        return True
