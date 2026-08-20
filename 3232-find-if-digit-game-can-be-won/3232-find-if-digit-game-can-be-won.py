class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum_single_dig = 0
        sum_double_dig = 0
        for num in nums:
            if num >=10:
                sum_single_dig += num
                
            else:
                sum_double_dig +=num
        return sum_single_dig> sum_double_dig or sum_double_dig>sum_single_dig 
            
                
                
