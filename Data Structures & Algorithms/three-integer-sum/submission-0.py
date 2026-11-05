class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zeroes = []
        nums.sort()
        for i in range(len(nums)-2):
            #we now need i = -(j+k) for them to sum up to 0
            j = i+1
            k = len(nums)-1
            while j<k:
                compliment = nums[j]+nums[k]
                
                if compliment < -nums[i]:
                    j+=1
                elif compliment > -nums[i]:
                    k -= 1
                else:
                    if [nums[i],nums[j],nums[k]] not in zeroes:
                        zeroes.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
        return zeroes