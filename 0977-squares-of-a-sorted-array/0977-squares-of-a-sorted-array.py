class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        num = []
        for n in nums:
            n = n*n
            num.append(n)

        num.sort()

        return num
