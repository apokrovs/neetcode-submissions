class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        seen = set()

        for i,c in enumerate(s):
            while c in seen:
                seen.remove(s[start])
                start+=1

            seen.add(c)
            max_len = max(max_len, i-start+1)
        return max_len



     