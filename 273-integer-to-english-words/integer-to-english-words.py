class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0 :
            return "Zero"
        below_20 = {
            0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
            7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve",
            13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
            18: "Eighteen", 19: "Nineteen"
        }
        
        tens = {
            2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 
            7: "Seventy", 8: "Eighty", 9: "Ninety"
        }
        
        thousands = ["", "Thousand", "Million", "Billion"]
        i = 0 
        def word(num: int) -> str:
            if num == 0:
                return ""
            elif num < 20:
                return below_20[num] + " "
            elif num < 100:
                return tens[num // 10] + " " + word(num % 10)
            else:
                return below_20[num // 100] + " Hundred " + word(num % 100)
        
        result = ""
        for i in range(len(thousands)):
            if num % 1000 != 0:
                result = word(num % 1000) + thousands[i] + " " + result
            num //= 1000
        
        return result.strip()