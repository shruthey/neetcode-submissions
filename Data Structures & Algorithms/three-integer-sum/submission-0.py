class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i, n in enumerate(nums):
            if n > 0:
                break

            if i > 0 and n == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                cur = nums[left] + nums[right] + n
                if cur == 0:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif cur < 0:
                    left += 1
                else:
                    right -= 1
        return res