class Solution:
    def reverseWords(self, s: str) -> str:
        word =""
        result = ""
        for char in s:
            if char == " ":
                result = result + word[::-1] + " "
                word = ""
            else:
                word = word + char
        
        result = result + word[::-1]

        return result
