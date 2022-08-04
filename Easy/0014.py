class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda s : len(s))
        answer = ""
        
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if strs[0][i] != s[i]:
                    return answer
            answer += strs[0][i]
        
        return answer
