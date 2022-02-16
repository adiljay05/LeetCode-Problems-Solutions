class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        ans = []
        for n in nums1:
            for m in nums2:
                if n==m:
                    ans.append(n)
        return ans