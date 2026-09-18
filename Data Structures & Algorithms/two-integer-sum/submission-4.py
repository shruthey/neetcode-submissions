class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {n: i for i, n in enumerate(nums)}
        
        for i, n in enumerate(nums):
            j = index.get(target - n)
            if j is not None and j != i:
                return [min(i, j), max(i, j)]