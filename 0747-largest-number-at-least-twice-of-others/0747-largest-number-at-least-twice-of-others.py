class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        a=max(nums)
        b = nums.index(a)
        for i in nums:
            if i!=a and i*2 >a :
                return -1
            
        return b