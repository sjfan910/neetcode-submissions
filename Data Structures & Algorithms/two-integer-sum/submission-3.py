class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            k = i
            for j in nums[i+1:]:
                k+=1
                holder = nums[i] + j
                if holder == target:
                    return [i, k]