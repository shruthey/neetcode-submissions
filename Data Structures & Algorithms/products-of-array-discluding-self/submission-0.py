class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = nums.count(0)
        product = 1
        
        if zeroes >= 2:
            return [0] * len(nums)
        elif zeroes == 1:
            zeroAt = nums.index(0)
            product = math.prod(nums[:zeroAt]+nums[zeroAt + 1:])
            return [int(product) if n == 0 else 0 for n in nums]
        else:
            product = math.prod(nums)
            return [int(product/n) for n in nums]