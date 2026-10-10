class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] < nums[left + 1]:
                left += 1
            elif nums[left] > nums[left + 1]:
                return nums[left + 1]
            if nums[right] > nums[right - 1]:
                right -= 1
            elif nums[right] < nums[right - 1]:
                return nums[right]
        return -1