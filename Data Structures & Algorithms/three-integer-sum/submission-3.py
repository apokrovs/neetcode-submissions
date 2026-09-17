class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            seen = set()
            j = i + 1
            while j < len(nums):
                need = - nums[i] - nums[j]
                if need in seen:
                    result.append([nums[i], need, nums[j]])
                    while j + 1 < len(nums) and nums[j] == nums[j+1]:
                        j+=1
                seen.add(nums[j])
                j+=1
        return result