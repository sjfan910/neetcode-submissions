class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        while nums[start]+nums[end] != target:
            if nums[start]+nums[end] < target:
                start += 1
            elif nums[start]+nums[end] > target:
                end -= 1
        return [start+1, end+1]