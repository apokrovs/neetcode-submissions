class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtracking(start:int, current:List[int], remaining:int):
            if remaining == 0:
                result.append(current[:])
                return
            if remaining < 0:
                return
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtracking(i, current, remaining-nums[i])
                current.pop()
        
        backtracking(0, [], target)
        return result
        