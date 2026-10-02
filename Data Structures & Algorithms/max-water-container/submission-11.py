class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_h = 0

        while left <= right:
            curr = min(heights[left], heights[right])*(right-left)
            max_h = max(curr, max_h)
            if max_h == 72:
                print(left, right)
            if heights[left] > heights[right]:
                right-=1
               
            else:
                left +=1
            
        return max_h



