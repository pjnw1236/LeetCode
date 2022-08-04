class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        d = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000} 
        for idx, char in enumerate(s[:-1]):
            if (char == "I") and (s[idx+1] in ["V", "X"]):
                answer -= d[char]
            elif (char == "X") and (s[idx+1] in ["L", "C"]):
                answer -= d[char]
            elif (char == "C") and (s[idx+1] in ["D", "M"]):
                answer -= d[char]
            else:
                answer += d[char]
        return answer+d[s[-1]]
