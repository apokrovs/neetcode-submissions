class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        i = 1
        for i in range(1,len(nums)+1):
            xor ^= i
            i+=1
        for num in nums:
            xor ^= num
        return xor
        