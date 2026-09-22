class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_freq = 0
        max_len = 0
        freqs = [0] * 26

        for r in range(len(s)):
            char_idx = ord(s[r]) - ord('A')
            freqs[char_idx] += 1
            max_freq = max(max_freq, freqs[char_idx])

            while (r - l + 1) - max_freq > k:
                freqs[ord(s[l]) - ord('A')] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len