class Solution:
    def intToRoman(self, num: int) -> str:
        self.ans = ""
        def changer(n):
            if n == 0 :
                return 
            if n < 5 :
                if n == 4 :
                    self.ans +="IV"
                else:
                    val = ("I"*n)
                    self.ans += val 
            elif n < 10 :
                if n%5 == 4 :
                    self.ans +="IX"
                    return 
                else:
                   n = n - 5 
                   self.ans +="V"
                   val = ("I"*n)
                   self.ans += val 
                return 
            elif n < 50:
                k = n % 10 
                l = n//10
                if l == 4:
                    self.ans += "XL"
                else:
                    val = ("X" * l)
                    self.ans += val 
                changer(k)
            elif n < 100 : 
                k = n % 10
                l = n // 10 
                if l == 9 :
                    self.ans += "XC"
                else:
                    self.ans +="L"
                    val = ("X" * (l-5))
                    self.ans += val 
                changer(k)
            elif n < 500 :
               k = n % 100
               l = n//100
               if l == 4:
                  self.ans += "CD"
               else :
                    val = ("C" * l)
                    self.ans += val 
               changer(k)
            elif n < 1000:
                k = n % 100
                l = n//100
                if l == 9:
                    self.ans += "CM"
                else:
                    self.ans +="D"
                    val = ("C" * (l-5))
                    self.ans += val 
                changer(k)
            else:
                k = n % 1000
                l = n // 1000
                val = ("M" * l)
                self.ans += val 
                changer(k)
        changer(num)
        return self.ans