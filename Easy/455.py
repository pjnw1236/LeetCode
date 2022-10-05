class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # s 쿠키 / g 아이
        g.sort() 
        s.sort() 
        
        answer=0
        pointer=0
        
        for i in range(len(g)):
            while True:
                if pointer >= len(s):
                    return answer
                if g[i] <= s[pointer]:
                    answer += 1
                    pointer += 1
                    break
                pointer += 1
        
        return answer
