from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        answer = 0 
        flag = False 
        strings=Counter(s) 
        for i in strings:
            if strings[i]%2 == 0:
                answer += strings[i] 
            else:
                answer += strings[i]-1 
                flag = True 
        if flag:
            return answer+1
        else:
            return answer
