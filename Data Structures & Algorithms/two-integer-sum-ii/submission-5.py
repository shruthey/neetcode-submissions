class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            add = nums[left] + nums[right]
            if add < target:
                left += 1
            elif add > target:
                right -= 1
            else:
                return [left + 1, right + 1]