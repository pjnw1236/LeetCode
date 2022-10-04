class Solution:    
    def countBits(self, n: int) -> List[int]:
        def bin_count(n):
            cnt = 0
            while n != 0:
                if n%2 == 1:
                    cnt += 1
                n//=2
            return cnt 
        
        answer = []
        for i in range(n+1):
            answer.append(bin_count(i))
        return answer;
