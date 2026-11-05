class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0
        for i in num_set:
            if i-1 in num_set:
                continue
            else:
                length = 1
                current = i
                while current+1 in num_set:
                    length += 1
                    current += 1
                longest = max(longest, length)
        return longest