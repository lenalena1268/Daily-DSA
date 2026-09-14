class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            answer.append(abs(left-right))

        return answer