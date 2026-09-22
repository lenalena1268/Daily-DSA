class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:

                # swap
                temp = s[left]
                s[left] = s[right]
                s[right] = temp

                # move towards middle
                left = left + 1
                right = right - 1