class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        total = 0
        for n in hours:
            if n >= target:
                total += 1

        return total
        