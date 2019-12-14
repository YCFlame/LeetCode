class Solution:
    less_than_20 = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen"
    ]
    tens = [
        "",
        "Ten",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety"
    ]
    thousands = [
        "","Thousand","Million","Billion"
    ]
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        rs = ""
        for i in range(len(self.thousands)):
            if num == 0:
                break
                
            if num % 1000:
                rs = self.helper(num % 1000) + self.thousands[i] + " " + rs
            
            num //= 1000
        
        return rs.strip()
    
    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.less_than_20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.less_than_20[num // 100] + " Hundred " + self.helper(num % 100)
