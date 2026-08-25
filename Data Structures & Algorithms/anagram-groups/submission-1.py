class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        alph = [0] * 26

        for word in strs:
            for c in word:
                alph[ord(c) - ord('a')] +=1
            key = tuple(alph)

            if key in table:
                table[key].append(word)
            else:
                table[key] = [word]
            alph = [0] * 26
        return list(table.values())