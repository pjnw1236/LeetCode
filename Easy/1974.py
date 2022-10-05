class Solution:
    def minTimeToType(self, word: str) -> int:
        typewriter = "abcdefghijklmnopqrstuvwxyz"
        answer = len(word) 
        word = "a" + word
        for i in range(1, len(word)):
            before = typewriter.index(word[i-1])
            after = typewriter.index(word[i])
            answer += min(abs(after-before), 26-abs(after-before))
        return answer
