class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = [target - i for i in nums]
        for j, comp in enumerate(complements):
            if comp in nums:
                i = nums.index(comp)
                if i != j:
                    return sorted([i, j])
