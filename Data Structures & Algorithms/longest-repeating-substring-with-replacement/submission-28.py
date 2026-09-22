class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        if len(s) ==1:
            return 1
        l = 0
        r = 1

        max_freq = 0
        max_len = 1
        max_freq_char = ""
        freqs = [0] * 26
        freqs[ord(s[0]) - ord('A')]+=1

        while r < len(s):
            char = s[r]
            freqs[ord(char) - ord('A')] +=1
            frequency = freqs[ord(char) - ord('A')]
            max_freq = max(frequency, max_freq)

            if r-l-k+1 <=  max_freq:
                max_len = max(max_len, r-l+1)
                r+=1
            else:
                freqs[ord(char) - ord('A')] -= 1
                freqs[ord(s[l]) - ord('A')] -=1
                l+=1


        return max_len
            


    