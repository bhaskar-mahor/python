class Solution:
    def maxArea(self,height):
        start, end = 0, len(height) - 1
        result = 0
        while start < end:
            result = max(min(height[start], height[end]) * (end - start), result)
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return result


obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))