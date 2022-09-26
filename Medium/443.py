class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0 
        cnt = 1 
        for i in range(1, len(chars)+1):
            if i < len(chars) and chars[i] == chars[i-1]:
                cnt += 1
            else:
                chars[idx] = chars[i-1] 
                idx += 1
                if cnt > 1:
                    for j in str(cnt):
                        chars[idx] = j 
                        idx += 1
                cnt = 1 
        return idx
