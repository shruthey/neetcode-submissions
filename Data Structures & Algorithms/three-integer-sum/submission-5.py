class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                return res
                
            if i > 0 and a == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            print (i, left, right)

            while left < right:
                add = a + nums[left] + nums[right]
                if add == 0:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif add < 0:
                    left += 1
                else:
                    right -= 1
            
        return res
