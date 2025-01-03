class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            dp[i], curr = 0, 0
            for j in range(i, len(s)):
                if curr == 0 and s[i] == '0':  # Leading zeros is not allowed
                    break
                curr = 10 * curr + int(s[j])
                if curr > k:  # If it exceeds, end the inner loop
                    break
                dp[i] += dp[j + 1]
                dp[i] %= mod

        return dp[0]