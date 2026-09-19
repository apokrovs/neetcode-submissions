class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        n = len(s)
        DP = [0] * (n+1)
        DP[0] = 1
        DP[1] = 1

        
        for i in range(2, n+1):
            if int(s[i-1])!=0:
                DP[i]+=DP[i-1]
            if 10<=int(s[i-2:i])<=26:
                DP[i]+=DP[i-2]
        return DP[n]
