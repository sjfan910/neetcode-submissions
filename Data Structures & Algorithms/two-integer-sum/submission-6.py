class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i,j in enumerate(nums):
            if target - int(j) not in seen:
                seen[j] = i
            else:
                return [seen[target-int(j)], i]