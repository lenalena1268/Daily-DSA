class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        ans = []
        for x in arr2:
            for y in arr1:
                if y == x:
                    ans.append(y)

        remaining = []
        for y in arr1:
            if y not in arr2:
                remaining.append(y)

        remaining.sort()
        for y in remaining:
            ans.append(y)

        return ans


