class Solution:
    def removeElement(self, nums, val):
        length = len(nums)
        if length == 0:
            return length
        index = 0
        for num in nums:
            if num == val:
                continue
            else:
                nums[index] = num
                index += 1
        return index


obj = Solution()
print(obj.removeElement([0,1,2,2,3,0,4,2],2))