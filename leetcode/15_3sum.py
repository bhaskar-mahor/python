class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()

        for i,digit in enumerate(nums):
            if i > 0 and digit == nums[i-1]:
                continue
            left , right = i+1, len(nums)-1
            while left < right:
                threeSum = digit + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([digit,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result
    
obj = Solution()
print(obj.threeSum([-1,0,1,2,-1,-4]))
print(obj.threeSum([0,1,1]))
print(obj.threeSum([0,0,0]))
