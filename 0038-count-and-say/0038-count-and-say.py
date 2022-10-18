class Solution:
    def countAndSay(self, n: int) -> str:
        dp = ["0"] * 31
        dp[1] = "1"
        for num in range(2, 31):
            save = ""
            cnt = 1
            for i in range(1, len(dp[num-1])):
                if dp[num-1][i] == dp[num-1][i-1]:
                    cnt += 1
                else:
                    save += str(cnt) + dp[num-1][i-1]
                    cnt = 1
            save += str(cnt) + dp[num-1][len(dp[num-1])-1]
            dp[num] = save 
        return dp[n]
                

        
        