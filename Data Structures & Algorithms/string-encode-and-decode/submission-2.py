class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#"
            encoded+=string
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            c = s[i]
            nums = ""
            while c.isdigit() and i < len(s):
                nums += c
                i+=1
                c = s[i]
            print(nums)
            if nums != "":
                num = int(nums)
            

            word = ""
            i+=1
            word = s[i:i+num]
            i+=num
            decoded.append(word)
        return decoded



