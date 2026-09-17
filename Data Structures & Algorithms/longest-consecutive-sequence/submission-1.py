class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = {}

        for num in nums:
            table[num] = 0
        overall = 0
        i = 0
        
        while i < len(nums):
            current = 0    
            if nums[i]-1 not in table:
                current = 1
                number = nums[i]
                while number+1 in table:
                    number+=1
                    current +=1
            i+=1
            overall = max(current, overall)
        return overall

            
        