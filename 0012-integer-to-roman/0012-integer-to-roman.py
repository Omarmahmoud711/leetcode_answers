class Solution(object):
    def intToRoman(self, num):
        roman_values = {
        1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC",
        100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"
        }
        res = ""
        for key in sorted(roman_values.keys(), reverse=True):
            now=num/key
            res=res + now*roman_values[key]
            num=num%key
        

        return res