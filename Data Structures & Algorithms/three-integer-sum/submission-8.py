class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            #skip a's dupes
            if i > 0 and nums[i - 1] == a:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                add = a + nums[left] + nums[right]
                if add == 0:
                    seen.add((a, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif add < 0:
                    left += 1
                else:
                    right -= 1
        return [list(t) for t in seen]