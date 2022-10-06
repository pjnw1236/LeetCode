class Solution:
    def maximumTime(self, time: str) -> str:
        answer = list(time)
        if answer[0] == "?":
            if answer[1] in "?0123":
                answer[0] = "2"
            else:
                answer[0] = "1"
        if answer[1] == "?":
            if answer[0] == "2":
                answer[1] = "3"
            else:
                answer[1] = "9"
        if answer[3] == "?":
            answer[3] = "5"
        if answer[4] == "?":
            answer[4] = "9"
        return "".join(answer)
                
