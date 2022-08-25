class Solution:
    def balancedStringSplit(self, s: str) -> int:
        answer=0
        R_cnt=0
        L_cnt=0
        for i in range(len(s)):
            if s[i] == "R":
                R_cnt += 1
            elif s[i] == "L":
                L_cnt += 1
            if (R_cnt == L_cnt) and (R_cnt) > 0:
                answer += 1
        return answer
