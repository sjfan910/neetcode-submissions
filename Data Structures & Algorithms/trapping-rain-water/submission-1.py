class Solution:
    def trap(self, height: List[int]) -> int:
        current = 0
        l = 0
        total = 0
        rightmax = []
        greatest = 0
        for i in height[::-1]:
            greatest = max(greatest, i)
            rightmax.append(greatest)
        rightmax = rightmax[::-1]
        for i in range(len(height)):
            if height[l] > height[i] and rightmax[i] > height[i]:
                total += min(height[l],rightmax[i])-height[i]
            else:
                l = i
        return total