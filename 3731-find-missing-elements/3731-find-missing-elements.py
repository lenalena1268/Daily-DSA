class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
      result = []
      small = min(nums)
      large = max(nums)
      for num in range(small,large+1):
        if num not in nums:
            result.append(num)
      return result
