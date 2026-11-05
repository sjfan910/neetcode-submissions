class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        maxvol = min(heights[i],heights[j])*(j-i)
        while j>i:
            if heights[i]<heights[j]:
                i+=1
                maxvol = max(maxvol, min(heights[i],heights[j])*(j-i))
            elif heights[j]<heights[i]:
                j-=1
                maxvol = max(maxvol, min(heights[i],heights[j])*(j-i))        
            else:
                i+=1
                maxvol = max(maxvol, min(heights[i],heights[j])*(j-i))
        return maxvol