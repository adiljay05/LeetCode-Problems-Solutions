class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = set(nums)
        for n in nums:
            if n == target:
                return True
        return False