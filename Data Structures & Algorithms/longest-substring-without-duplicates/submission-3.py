class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0

        for i,c in enumerate(s):
            word = s[start:i]
            while c in word:
                start+=1
                word = s[start:i]
            max_len = max(max_len, i-start+1)
        return max_len



     