class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result, last = 0, 0
        for i in s:
            curr = roman[i]
            result += curr
            if curr > last:
                result -= 2*last
            last = curr
        return result   
       
"""
        mapper = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40, 
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        before = None
        for c in s:
            if before is not None:
                value = mapper.get(before + c, 0)
                if value > 0:
                    result += value
                    before = None
                    continue
                else:
                    result += mapper[before]
                    before = c
            else:
                before = c
        
        if before is not None:
            result += mapper[before]
        return result
"""
