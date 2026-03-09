class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j][k]: i zeros used, j ones used, last element is k
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base: arrays of all 0s or all 1s (up to limit length)
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
        
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                if i > limit:
                    dp[i][j][0] = (dp[i][j][0] - dp[i-limit-1][j][1]) % MOD
                
                dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                if j > limit:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j-limit-1][0]) % MOD
        
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD