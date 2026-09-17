class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            running_sum.append(total)

        return running_sum