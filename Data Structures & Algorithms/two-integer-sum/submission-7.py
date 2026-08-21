class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for i,n in enumerate(nums):
            left = target - n
            if left in table:
                return [table[left], i]
            table[n] = i
