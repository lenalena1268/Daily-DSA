class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result=[]
        for n in nums1:
            if n in nums2 and n not in result:
                result.append(n)

        return result