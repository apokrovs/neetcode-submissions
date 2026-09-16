class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product =1
        zero_count = 0
        
        for num in nums:
            if num == 0:
                zero_count +=1
                continue
            product *= num
        result = []

        if zero_count > 1:
            return [0]*len(nums)

        for num in nums:
            if zero_count > 0:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(product//num)
        
        return result
        