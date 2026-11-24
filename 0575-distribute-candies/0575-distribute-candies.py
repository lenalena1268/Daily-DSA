class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
       half = len(candyType)//2
       unique =len( set(candyType))
       if unique < half:
        return unique
       else:
        return half

    